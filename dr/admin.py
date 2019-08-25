from django.contrib import admin

from dr.models import Room, User, Reservation
from dr.google_calendar import Calendar
from django.contrib import messages
from dr.views import validate_reservation_date


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'status')
    list_filter = ['status', 'capacity']


admin.site.register(Room, RoomAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'indeks', 'permission', 'group')
    list_filter = ['group', 'permission']


admin.site.register(User, UserAdmin)


class ReservationAdmin(admin.ModelAdmin):
    ordering = ['-start_reservation', 'room']

    list_display = ('user', 'room', 'start_reservation', 'end_reservation', 'status')
    list_filter = ['status', 'user', 'room']

    fieldsets = (
        (None, {
            'fields': ('user', 'room', 'description', 'start_reservation', 'end_reservation', 'status')
        }),
    )

    def response_post_save_change(self, request, obj):
        if request.POST.get('_accept'):
            calendar = Calendar()
            obj.status = 'a'
            summary = str(obj.room) + " " + str(obj.user)
            sd = str(obj.start_reservation)
            sd = sd[:10] + 'T' + sd[11:]
            ed = str(obj.end_reservation)
            ed = ed[:10] + 'T' + ed[11:]
            print("++++++++++++++++++++++++++++++++", obj,validate_reservation_date(obj))
            if not validate_reservation_date(obj):
                print("date is not valid with other reservations")
                messages.add_message(request, messages.WARNING, "Data collision exists for " + str(obj.user) + " "
                                 + str(obj.room) + ", changes were not saved.")

            if obj.status == 'a' and not obj.googleId and validate_reservation_date(obj):
                event_id = calendar.addEvent(summary, sd, ed, obj.description)
                obj.googleId = event_id
                print("----", obj.googleId)
                obj.save()
                print("zapisano google id !!!!")
            return super().response_post_save_change(request, obj)
        elif request.POST.get('_reject'):
            obj.status = 'r'
            obj.save()
            return super().response_post_save_change(request, obj)
        elif request.POST.get('_save'):
            obj.status = 'i'
            obj.save()
            return super().response_post_save_change(request, obj)


admin.site.register(Reservation, ReservationAdmin)
admin.site.site_header = "DRIMn Reserve"
admin.site.site_title = "DRIMn Reserve"
