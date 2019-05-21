from django.contrib import admin

# Register your models here.
from dr.models import Room,  User, Reservation
from dr.google_calendar import Calendar

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

    def response_post_save_change(self, request, obj):
        calendar = Calendar()
        print("Gitesik")
        #tu sie bedzie działo wstawianie do kalendarza 
        print(obj)
        calendar.addEvent("15")
        costam = Reservation.objects.filter()
        
        return super().response_post_save_change(request, obj)

admin.site.register(Reservation, ReservationAdmin)
admin.site.site_header = "DRIMn Reserve"
admin.site.site_title = "DRIMn Reserve"
