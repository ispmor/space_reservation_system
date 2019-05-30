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
from .models import User
from django.contrib.auth.models import User as muser
from django.contrib.auth.hashers import make_password

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
def failed_register(request):
    return render(request, 'failed_register.html')
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
        print(request.user)
        if form.is_valid():
            print("form is valid")
            if request.user.is_authenticated:
                reservation = Reservation()
                guest = User.objects.get(username=request.user.username)
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

def register(request):
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