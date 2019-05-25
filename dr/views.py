from dr.models import Room, Reservation, User
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreateForm, ReservationForm


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
    return render(request, 'failed_reservation.html')
# dziala, pozostało dołączyć do odpowiednich stron z odpowiednimi templatkami.
def email(request):

    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['startapplocha86@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return register(request)


def reservation(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        print("jestem w post")
        if form.is_valid():
            print("form is valid")
            if request.user.is_authenticated:
                reservation = Reservation()
                guest = User.objects.get(first_name=request.user)
                reservation.user = guest
                reservation.room = form.cleaned_data.get('room')
                reservation.status = 'i'
                reservation.start_reservation = form.cleaned_data.get('start_reservation')
                reservation.end_reservation = form.cleaned_data.get('end_reservation')
                print("rezerwacja")
                print(reservation.status)
                print(reservation.start_reservation)
                print(reservation.end_reservation)
                print(reservation)
                reservation.save()
                return HttpResponseRedirect('/')

            else:
                print("niezalogowany uzytkownik")
                #reservation = form.save()
                #reservation.save()
                return HttpResponseRedirect('/')
        else :
            print("szajse! form nie valid")
            return HttpResponseRedirect('/dr/failed_reservation')
    
    else :
        form = ReservationForm()
        return render(request, 'reservation.html',{'form': form})















class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreateForm()
        return render(request, 'signup.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            first_name = userObj['first_name']
            second_name = userObj['second_name']
            email =  userObj['email']
            password =  userObj['password']
            group = userObj['group']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(first_name, second_name, email, password, group)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserCreateForm()
    return render(request, 'register.html', {'form' : form})    
    # return render(request, 'register.html')
# def register(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.save()
#             User.objects.create(user=new_user)
#             cd = form.cleaned_data
#             user = authenticate(
#                 request,
#                 username=cd['username'],
#                 password=cd['password1'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('login/edit/')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid Login')
#     else:
#         form = UserForm()
#         args = {'form': form}
#         return render(request, 'reg_form.html', args)