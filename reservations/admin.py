
from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):

    list_display = ('user', 'room', 'start_reservation', 'end_reservation')
    list_filter = ['user', 'room']
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
            print("++++++++++++++++++++++++++++++++", obj)
            if obj.status == 'a' and not obj.googleId:
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