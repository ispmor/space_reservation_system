from django.shortcuts import render
from .forms import ReservationForm
from .models import Reservation
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
# Create your views here.
class ReservationCreateView(BSModalCreateView):
    template_name = 'reservation/modals/create.html'
    form_class = ReservationForm
    success_message = 'Success: Reservation was created.'


class ReservationUpdateView(BSModalUpdateView):
    model = Reservation
    template_name = 'reservation/modals/update.html'
    form_class = ReservationForm
    success_message = 'Success: Reservation was updated.'


class ReservationReadView(BSModalReadView):
    model = Reservation
    template_name = 'reservation/modals/read.html'


class ReservationDeleteView(BSModalDeleteView):
    model = Reservation
    template_name = 'reservation/modals/delete.html'
    success_message = 'Success: Reservation was deleted.'




#legacy:
# def failed_reservation(request):
#     if request.user.is_authenticated:
#         return render(request, 'failed_reservation.html')
#     else:
#         return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)

# def failed_register(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)
#     else:
#         return render(request, 'failed_register.html')


# def reservation(request):
#     if request.user.is_authenticated:
#         form = ReservationForm()
#         if request.method == 'POST':
#             form = ReservationForm(request.POST)
#             if form.is_valid():
#                 reservation = Reservation()
#                 guest = User.objects.get(username=request.user.username)
#                 reservation.user = guest
#                 reservation.room = form.cleaned_data.get('room')
#                 reservation.status = 'i'
#                 reservation.start_reservation = form.cleaned_data.get('start_reservation')
#                 reservation.end_reservation = form.cleaned_data.get('end_reservation')
#                 reservation.description = form.cleaned_data.get('description')
#                 if not validate_reservation_date(reservation) :
#                     return HttpResponseRedirect(settings.FAILED_RESERVATION_URL)
#                 reservation.save()
#                 return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)
#             else :
#                 return HttpResponseRedirect(settings.FAILED_RESERVATION_URL)
#         else :
#             form = ReservationForm()
#             return render(request, 'reservation.html',{'form': form})
#     else:
#         return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

# def validate_reservation_date(reservation):
#     reservation_list = Reservation.objects.filter(room=reservation.room, status='a').order_by("-start_reservation")
    
#     if 0 < len(reservation_list) <= 25 :
#         number_of_checked_reservations = len(reservation_list) -1
#     elif len(reservation_list) > 0 :
#         number_of_checked_reservations = 25
#     else:
#         number_of_checked_reservations = 0
#     for r in reservation_list[: number_of_checked_reservations]:
#         print("=======", r.start_reservation, reservation.start_reservation)
#         print("+++++++", r.end_reservation, reservation.end_reservation )
#         if r.start_reservation < reservation.start_reservation < r.end_reservation or r.start_reservation < reservation.end_reservation < r.end_reservation :
#             return False
#     return True

            
# def reservations(request):
#     now = timezone.now()
#     if request.user.is_authenticated:
#         now = timezone.now()
#         user = request.user
#         reservations = Reservation.objects.filter(user=User.objects.get(username=user.username).id, archived = False, end_reservation__gte = now - timedelta(hours = 1))
#         context = {
#             "reservations": reservations
#         }
#         if request.GET.get('delete'):
#             id = request.GET.get('id')
#             instance = Reservation.objects.filter(id=id)
#             start = instance[0].start_reservation
#             if now + timedelta(hours=24) <= start: 
#              if instance[0].googleId:
#                  calendar = Calendar()
#                  calendar.deleteEvent(instance[0].googleId)
#              instance.delete()
#             return HttpResponseRedirect(settings.RESERVATION_URL)
#         return render(request, 'reservations.html', context=context)
#     else:
#         return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

# def concierge(request):
#     if request.method == 'GET' and request.user.is_authenticated:
#         now = timezone.now()
#         reservations = Reservation.objects.filter(
#             start_reservation__lte = now + timedelta(hours = 24),
#             end_reservation__gte = now - timedelta(hours = 1),
#             archived = False,
#             status = 'a')
#         context = {
#             "reservations": zip(reservations, map(lambda r: getState(r), reservations)), # not sure why it does not work xD 
#         }
#         return render(request, 'concierge.html', context=context)
#     else:
#         return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
# def email(request):
#     subject = 'Thank you for registering to our site'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['startapplocha86@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list )
#     return register(request)

# def clear_users(request):
#     User.objects.all().delete()
#     print("User database was simply wiped out ~ Thanos 2019")
#     return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)

# def newCalendar(request, summary):
#     calendar = Calendar()
#     calendar.insertNewCalendar(summary)
#     return HttpResponseRedirect(settings.INDEX_REDIRECT_URL)

# def get_availale_time(request):
#     return JsonResponse(getAvailableTime())