from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'title', 'message')
    list_filter = ['email']


admin.site.register(Contact, ContactAdmin)