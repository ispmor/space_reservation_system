

from django.db import models

import uuid

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, help_text='Unique ID for this particular Reservation')
    room = models.ForeignKey("rooms.Room", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey("users.CustomUser", on_delete=models.SET_NULL, null=True)
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
    description = models.CharField(blank=False, max_length=1024, default="I want to book this room because: ")
    start_reservation = models.DateTimeField(null=True, blank=True)
    end_reservation = models.DateTimeField(null=True, blank=True)
    googleId = models.TextField(null=True, blank=True)
    archived = models.BooleanField(blank = True, null = True, default = False)
    help_text = "Reservation status",
    default='i'

    def __str__(self):
        return f'{self.user} {self.room}'

