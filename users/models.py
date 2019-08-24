from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    indeks = models.IntegerField(blank = True, null=True)
    permission = models.CharField(
        max_length = 1,
        choices = (
        ('b', 'Banned'),
        ('a', 'Allowed'),
    ),
        blank = True,
        help_text = "Is User allowed to create a reservation"
    )
    group = models.CharField(
        max_length = 1,
        choices = (
        ('s', 'Student'),
        ('l', 'Lecturer'),
        ('e', 'External'),
    ),
        blank = True,
        help_text = "To which group does User qualify"
    )
    archived = models.BooleanField(blank = True, null = True, default = False)
    pass

    def __str__(self):
        return self.email