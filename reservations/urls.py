from django.urls import path

from .views import ReservationUpdateView, ReservationCreateView, ReservationDeleteView, ReservationReadView

urlpatterns = [
    path('read/', ReservationReadView.as_view(), name='read'),
    path('update/', ReservationUpdateView.as_view(), name='update'),
    path('create/', ReservationCreateView.as_view(), name='create'),
    path('delete/', ReservationDeleteView.as_view(), name='delete'),
]
