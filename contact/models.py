from django.db import models

class ContactRequest(models.Model):
    title = models.CharField(null = False, blank = False, max_length = 150)
    email = models.EmailField(null = True)
    message = models.CharField(null = False, blank = False, max_length = 450)
