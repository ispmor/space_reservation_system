from django.urls import path

from .views import ReservationUpdateView, ReservationCreateView, ReservationDeleteView, ReservationReadView, ReservationListView, reservation
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse

urlpatterns = [
    path('read/<uidb64>', ReservationReadView.as_view(), name='read_reservation'),
    path('update/<uidb64>', ReservationUpdateView.as_view(), name='update_reservation'),
    path('create/', ReservationCreateView.as_view(), name='create_reservation'),
    path('delete/<uidb64>', ReservationDeleteView.as_view(), name='delete_reservation'),
    path('list/', ReservationListView.as_view(), name='list'),
    path('', reservation, name='reservation'),
]
