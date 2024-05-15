from django.contrib import admin
from .models import Service, Appointment, Article

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'price')
    search_fields = ('title',)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'appointment_date', 'accepted')
    list_filter = ('accepted',)
    actions = ['accept_appointments', 'reject_appointments']

    def accept_appointments(self, request, queryset):
        queryset.update(accepted=True)

    def reject_appointments(self, request, queryset):
        queryset.delete()

admin.site.register(Service, ServiceAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Article)

