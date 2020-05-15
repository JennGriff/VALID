from django.contrib import admin
from .models import EmergencyReasons, Emergency, Scheduled, ScheduledReasons

admin.site.register(EmergencyReasons)
admin.site.register(Emergency)
admin.site.register(ScheduledReasons)
admin.site.register(Scheduled)
