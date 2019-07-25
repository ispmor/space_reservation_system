from django.contrib import admin

from dr.models import Room,  User, Reservation
from dr.google_calendar import Calendar

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'status')
    list_filter = ['status', 'capacity']
admin.site.register(Room, RoomAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'indeks', 'permission', 'group')
    list_filter = ['group', 'permission']
admin.site.register(User, UserAdmin)

class ReservationAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'room', 'start_reservation', 'end_reservation')
    list_filter = ['user', 'room']

    def response_post_save_change(self, request, obj):
        calendar = Calendar()
        summary = str(obj.room) + " " + str(obj.user)
        sd = str(obj.start_reservation)
        sd = sd[:10] + 'T' + sd[11:]
        ed = str(obj.end_reservation)
        ed = ed[:10] + 'T' + ed[11:]

        print("++++++++++++++++++++++++++++++++", obj)

        print(sd)
        print(ed)
        if obj.status == 'a' and not obj.googleId:
            event_id = calendar.addEvent(summary, sd, ed, obj.description)
            obj.googleId = event_id
            print("----", obj.googleId)
            obj.save()
            print("zapisano google id !!!!")
            
        
        return super().response_post_save_change(request, obj)

admin.site.register(Reservation, ReservationAdmin)
admin.site.site_header = "DRIMn Reserve"
admin.site.site_title = "DRIMn Reserve"
