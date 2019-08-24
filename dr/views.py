from dr.models import Room, Reservation, User, ContactRequest
from django.core.mail import send_mail
from django.conf import settings
import pytz
from django.utils import timezone

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ( ReservationForm, ContactForm, CustomUserCreationForm, CustomAuthenticationForm) 
from . import models
from django.contrib.auth.models import User as muser
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta
from.google_calendar import Calendar, getAvailableTime
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)



class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'modals/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('index')
    def post(self, request):
        template_name = 'index.html'
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            first_name = userObj['first_name']
            last_name = userObj['last_name']
            email =  userObj['email']
            password =  userObj['password']
            group = userObj['group']
            user = User(username=username, first_name=first_name, last_name=last_name, email=email, group=group)
            user_abstr = muser(username=username, first_name=first_name, last_name=last_name, email=email,  password=make_password(password))
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                user.save()
                user_abstr.save()
                user = authenticate(username = username, password = password)
                login(request, user)
                context = {'success_message': "You successfully created account"}
            else:
                context = {'success_message':"Email is already in use"}
        else:
            context = {'success_message': "Something went wrong"}
        return render(request, template_name, context)
        


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'modals/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('/')

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class ContactView(BSModalCreateView):
    form_class = ContactForm
    template_name = 'modals/contact.html'
    success_message = 'Success: You successfully contacted us!.'
    success_url = reverse_lazy('/')

    def post(self, request):
        base_form  = ContactForm()
        form = ContactForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                contact_request = ContactRequest(title = form.cleaned_data['title'], message = form.cleaned_data['message'], email = request.user.email)
            elif form.cleaned_data['email'] != '':
                contact_request = ContactRequest(title = form.cleaned_data['title'], message = form.cleaned_data['message'], email = form.cleaned_data['email'])
            else:
                return render(request, 'index.html', {'form': base_form, 'message': 'Mail not provided'})
            contact_request.save()
            send_mail(contact_request.title, contact_request.message, contact_request.email,  [settings.EMAIL_HOST_USER, contact_request.email])
        else:
            return render(request, 'index.html', {'form': base_form})
        return render(request, 'index.html', {'form': base_form, 'success_message': 'You successfuly contacted us! Now wait for an answer :)'})

class Index(generic.ListView):
    def get(self, request):
        template_name = 'index.html'
        now = timezone.now()
        if (request.user.is_authenticated):
            user = request.user
            reservations = Reservation.objects.filter(user=User.objects.get(username=user.username).id, archived = False, end_reservation__gte = now - timedelta(hours = 1))
            context = {"reservations": reservations}
            return render(request, template_name, context)
        return render(request, template_name)


class ReservationCreateView(BSModalCreateView):
    template_name = 'modals/create_reservation.html'
    form_class = ReservationForm
    success_message = 'Success: Reservation was created.'
    success_url = reverse_lazy('index')


class ReservationUpdateView(BSModalUpdateView):
    model = Reservation
    template_name = 'modals/update_reservation.html'
    form_class = ReservationForm
    success_message = 'Success: Reservation was updated.'
    success_url = reverse_lazy('index')


class ReservationReadView(BSModalReadView):
    model = Reservation
    template_name = 'modals/read_reservation.html'


class ReservationDeleteView(BSModalDeleteView):
    model = Reservation
    template_name = 'modals/delete_reservation.html'
    success_message = 'Success: Reservation was deleted.'
    success_url = reverse_lazy('index')



def failed_reservation(request):
    if request.user.is_authenticated:
        return render(request, 'failed_reservation.html')
    else:
        return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)

def failed_register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)
    else:
        return render(request, 'failed_register.html')


def reservation(request):
    if request.user.is_authenticated:
        form = ReservationForm()
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                reservation = Reservation()
                guest = User.objects.get(username=request.user.username)
                reservation.user = guest
                reservation.room = form.cleaned_data.get('room')
                reservation.status = 'i'
                reservation.start_reservation = form.cleaned_data.get('start_reservation')
                reservation.end_reservation = form.cleaned_data.get('end_reservation')
                reservation.description = form.cleaned_data.get('description')
                if not validate_reservation_date(reservation) :
                    return HttpResponseRedirect(settings.FAILED_RESERVATION_URL)
                reservation.save()
                return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)
            else :
                return HttpResponseRedirect(settings.FAILED_RESERVATION_URL)
        else :
            form = ReservationForm()
            return render(request, 'reservation.html',{'form': form})
    else:
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

def validate_reservation_date(reservation):
    reservation_list = Reservation.objects.filter(room=reservation.room, status='a').order_by("-start_reservation")
    
    if 0 < len(reservation_list) <= 25 :
        number_of_checked_reservations = len(reservation_list) -1
    elif len(reservation_list) > 0 :
        number_of_checked_reservations = 25
    else:
        number_of_checked_reservations = 0
    for r in reservation_list[: number_of_checked_reservations]:
        print("=======", r.start_reservation, reservation.start_reservation)
        print("+++++++", r.end_reservation, reservation.end_reservation )
        if r.start_reservation < reservation.start_reservation < r.end_reservation or r.start_reservation < reservation.end_reservation < r.end_reservation :
            return False
    return True

            
def reservations(request):
    now = timezone.now()
    if request.user.is_authenticated:
        now = timezone.now()
        user = request.user
        reservations = Reservation.objects.filter(user=User.objects.get(username=user.username).id, archived = False, end_reservation__gte = now - timedelta(hours = 1))
        context = {
            "reservations": reservations
        }
        if request.GET.get('delete'):
            id = request.GET.get('id')
            instance = Reservation.objects.filter(id=id)
            start = instance[0].start_reservation
            if now + timedelta(hours=24) <= start: 
             if instance[0].googleId:
                 calendar = Calendar()
                 calendar.deleteEvent(instance[0].googleId)
             instance.delete()
            return HttpResponseRedirect(settings.RESERVATION_URL)
        return render(request, 'reservations.html', context=context)
    else:
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)


def getState(r): 
    now = timezone.now()
    if r.end_reservation < now:
        'Ended'
    elif r.start_reservation > now:
        'Starting soon'
    else:
        'In progress' 

def concierge(request):
    if request.method == 'GET' and request.user.is_authenticated:
        now = timezone.now()
        reservations = Reservation.objects.filter(
            start_reservation__lte = now + timedelta(hours = 24),
            end_reservation__gte = now - timedelta(hours = 1),
            archived = False,
            status = 'a')
        context = {
            "reservations": zip(reservations, map(lambda r: getState(r), reservations)), # not sure why it does not work xD 
        }
        return render(request, 'concierge.html', context=context)
    else:
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

def register(request):
    template_name = "register.html"
    if request.user.is_authenticated:
        return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)
    else:
        if request.method == 'POST':
            form = UserCreateForm(request.POST)
            if form.is_valid():
                userObj = form.cleaned_data
                username = userObj['username']
                first_name = userObj['first_name']
                last_name = userObj['last_name']
                email =  userObj['email']
                password =  userObj['password']
                group = userObj['group']
                user = User(username=username, first_name=first_name, last_name=last_name, email=email, group=group)
                user_abstr = muser(username=username, first_name=first_name, last_name=last_name, email=email,  password=make_password(password))
                if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    user.save()
                    user_abstr.save()
                    user = authenticate(username = username, password = password)
                    login(request, user)
                    return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)
                else:
                    return HttpResponseRedirect(settings.FAILED_REGISTER_URL)
        else:
            form = UserCreateForm()
        return render(request, template_name, {'form' : form})
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)
    else:
        return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['startapplocha86@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return register(request)

def clear_users(request):
    User.objects.all().delete()
    print("User database was simply wiped out ~ Thanos 2019")
    return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)

def newCalendar(request, summary):
    calendar = Calendar()
    calendar.insertNewCalendar(summary)
    return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)

def get_availale_time(request):
    return JsonResponse(getAvailableTime())
