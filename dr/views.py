from django.shortcuts import render
from dr.models import Room, Reservation, User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

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
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def forgot_password(request):
    return render(request, 'forgot_password.html')

# dziala, pozostało dołączyć do odpowiednich stron z odpowiednimi templatkami.
def email(request):

    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['startapplocha86@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return register(request)