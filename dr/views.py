from dr.models import Room, Reservation, User
from django.core.mail import send_mail
from django.conf import settings
import pytz
from django.utils import timezone

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreateForm, ReservationForm
from .models import User
from django.contrib.auth.models import User as muser
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta
from.google_calendar import Calendar

def index(request):
    """View function for home page of system website"""

    #Generate counts of some of the main objects
    num_rooms = Room.objects.all().count()
    num_reservations = Reservation.objects.all().count()
    num_users = User.objects.all().count()

    # Available rooms ( status = 'a')
    num_rooms_available = Room.objects.filter(status='a').count()

    context = {
        'num_rooms' : num_rooms,
        'num_reservations': num_reservations,
        'num_users' : num_users,
        'num_rooms_available' : num_rooms_available, 
    }
    return render(request, 'index.html', context=context)

def failed_reservation(request):
    if request.user.is_authenticated:
        return render(request, 'failed_reservation.html')
    else:
        return HttpResponseRedirect('/')

def failed_register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
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
                    return HttpResponseRedirect('/dr/failed_reservation')
                reservation.save()
                return HttpResponseRedirect('/')
            else :
                return HttpResponseRedirect('/dr/failed_reservation')
        else :
            form = ReservationForm()
            return render(request, 'reservation.html',{'form': form})
    else:
        return HttpResponseRedirect('/dr/login')

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
        
    if request.user.is_authenticated:
        user = request.user
        reservations = Reservation.objects.filter(user=User.objects.get(username=user.username).id)
        context = {
            "reservations": reservations
        }
        if request.GET.get('delete'):
            id = request.GET.get('id')
            instance = Reservation.objects.filter(id=id)
            
            now = timezone.now()
            start = instance[0].start_reservation

            if now + timedelta(hours=24) <= start: 
             if instance[0].googleId:
                 print("---- deletin - googleId ----", instance[0].googleId)
                 calendar = Calendar()
                 calendar.deleteEvent(instance[0].googleId)
             print("---- deleting ----",id)
             instance.delete()  
        return render(request, 'reservations.html', context=context)
    else:
        return HttpResponseRedirect('/dr/login')



def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dr')
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
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/dr/failed_reservation')
        else:
            form = UserCreateForm()
        return render(request, 'register.html', {'form' : form})
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

    # def email(request):
    #     subject = 'Thank you for registering to our site'
    # message = ' it  means a world to us '
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['startapplocha86@gmail.com',]
    # send_mail( subject, message, email_from, recipient_list )
    # return register(request)

def clear_users(request):
    User.objects.all().delete()
    print("User database was simply wiped out ~ Thanos 2019")
    return HttpResponseRedirect('/')
    