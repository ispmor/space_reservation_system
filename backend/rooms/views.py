from django.shortcuts import render
from .models import Room
from django.urls import reverse_lazy
from django.views import generic
from .serializers import RoomSerializer
from rest_framework import generics

from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
# Create your views here.
class RoomListView(generic.ListView):
    model = Room
    template_name = 'room/list.html'
    success_message = 'Success: Rooms found.'
    success_url = reverse_lazy('home')



class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer