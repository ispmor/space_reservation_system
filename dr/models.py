from django.db import models

from django.urls import reverse

class Room(models.Model):
    name = models.CharField(max_length=200)
    equipement = models.TextField(max_length=1000, help_text='Enter a brief description of the room')
    capacity = models.IntegerField()
    ROOM_STATUS = (
        ('i', 'In Use'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=ROOM_STATUS,
        blank=True,
        default='a',
        help_text='Room availability',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this room."""
        return reverse('room-detail', args=[str(self.id)])

    

import uuid
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular User')
    username = models.CharField(max_length=150, null=False, default='nick')
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=50, null=False)
    indeks = models.IntegerField(blank = True, null=True)
    email = models.CharField(max_length=150, null=False, default='x515692@nwytg.net')
    PERMISSION = (
        ('b', 'Banned'),
        ('a', 'Allowed'),
    )
    permission = models.CharField(
        max_length = 1,
        choices = PERMISSION,
        blank = True,
        help_text = "Is User allowed to create a reservation"
    )
    groups = (
        ('s', 'Student'),
        ('l', 'Lecturer'),
        ('e', 'External'),
    )
    group = models.CharField(
        max_length = 1,
        choices = groups,
        blank = True,
        help_text = "To which group does User qualify"
    )
    archived = models.BooleanField(blank = True, null = True, default = False)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}, {self.indeks}'

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, help_text='Unique ID for this particular Reservation')
    room = models.ForeignKey("Room", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    STATUS_OF_RESERVATION = (
        ('a', 'Accepted'),
        ('r', 'Rejected'),
        ('i', 'In Progress'),
    )
    status = models.CharField(
        max_length = 1,
        choices = STATUS_OF_RESERVATION,
        blank = True,
        help_text = "Reservation status"
    )
    description = models.CharField(blank=False, max_length=1024, default="I want to reserve this room because: ")
    start_reservation = models.DateTimeField(null=True, blank=True)
    end_reservation = models.DateTimeField(null=True, blank=True)
    googleId = models.TextField(null=True, blank=True)
    archived = models.BooleanField(blank = True, null = True, default = False)

    def __str__(self):
        return f'{self.user} {self.room}'