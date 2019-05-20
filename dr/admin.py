from django.contrib import admin

# Register your models here.
from dr.models import Room,  User, Reservation

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'status')
    list_filter = ['status', 'capacity']
admin.site.register(Room, RoomAdmin)
#admin.site.register(RoomInstance)

#class RoomInstanceAdmin(admin.ModelAdmin):
#    list_display = ('room', 'status', 'end_reservation')
#    list_filter = ['status']
#
#admin.site.register(RoomInstance, RoomInstanceAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'indeks', 'permission', 'group')
    list_filter = ['group', 'permission']
admin.site.register(User, UserAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'start_reservation', 'end_reservation')
    list_filter = ['user', 'room']

admin.site.register(Reservation, ReservationAdmin)
admin.site.site_header = "DRIMn Reserve"
admin.site.site_title = "DRIMn Reserve"
