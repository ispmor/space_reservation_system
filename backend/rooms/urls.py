from django.conf import settings
from django.urls import path, include
from .views import RoomListView
urlpatterns = [
    path('list/', RoomListView.as_view(), name='room-list'),
]