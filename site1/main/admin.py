from django.contrib import admin
from .models import Service, Appointment
from .models import Question
from .models import Article
from .models import Testimonial
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'price')
    search_fields = ('title',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'appointment_date', 'appointment_time', 'service', 'status', 'approved')
    list_filter = ('status',)
    actions = ['accept_appointments', 'reject_appointments']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    def accept_appointments(self, request, queryset):
        queryset.update(status='Approved', approved=True)
    accept_appointments.short_description = "Accept selected appointments"

    def reject_appointments(self, request, queryset):
        queryset.update(status='Rejected', approved=False)
    reject_appointments.short_description = "Reject selected appointments"



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_answered', 'created_at')
    list_filter = ('is_answered', 'created_at')
    search_fields = ('full_name', 'email', 'message')
    readonly_fields = ('created_at',)
    fields = ('full_name', 'email', 'message', 'response', 'is_answered', 'created_at')

    def save_model(self, request, obj, form, change):
        if 'response' in form.changed_data:
            obj.is_answered = True
        super().save_model(request, obj, form, change)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'created_at', 'updated_at')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Testimonial)