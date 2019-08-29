
from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'status')
    list_filter = ['status', 'capacity']


admin.site.register(Room, RoomAdmin)