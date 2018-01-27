from django.contrib import admin
from .models import Registrant

class RegistrantAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'session1', 'session2', 'session3', 'meals', 'telephone', 'email')
    search_fields = ('firstname', 'lastname', 'telephone', 'email')
    list_filter = ('session1', 'session2', 'session3', 'meals')

admin.site.register(Registrant, RegistrantAdmin)

# Register your models here.
