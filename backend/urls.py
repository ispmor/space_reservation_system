"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, MessageViewSet
from .rooms.viewsets import RoomViewSet
from .contact.viewsets import ContactViewSet
from .reservations.viewsets import ReservationViewSet
from .users.viewsets import UserViewSet
from .users.urls import urlpatterns as user_url
from .pages.urls import urlpatterns as page_url
from .rooms.urls import urlpatterns as room_url
from .reservations.urls import urlpatterns as reservation_url
from .contact.urls import urlpatterns as contact_url

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('rooms', RoomViewSet)
router.register('reservations', ReservationViewSet)
router.register('users', UserViewSet)
router.register('contact', ContactViewSet)

urlpatterns = [
    # http://localhost:8000/
    path('', index_view, name='index'),
    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
    path('pages', include(page_url)),
    path('rooms', include(room_url)),
    path('reservations', include(reservation_url)),
    path('contact', include(contact_url)),
    path('users', include(user_url)),
]


