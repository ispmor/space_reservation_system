from django.contrib import admin
from .models import ContactRequest

class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'title', 'message')
    list_filter = ['email']


admin.site.register(ContactRequest, ContactRequestAdmin)