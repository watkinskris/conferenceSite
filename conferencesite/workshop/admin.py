from django.contrib import admin
from .models import Workshop

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('session_num', 'workshop_name', 'room_num', 'start_time', "end_time")
    list_filter = ('session_num', 'workshop_name', 'room_num', 'start_time', "end_time")

admin.site.register(Workshop, WorkshopAdmin)