from django.contrib import admin
from .models import Service, Appointment
from .models import Article
from .models import Testimonial
from .models import Question
from django.conf import settings
from django.core.mail import send_mail

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'price')
    search_fields = ('title',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'appointment_date', 'appointment_time', 'service', 'status', 'approved')
    list_filter = ('status', 'approved')
    actions = ['accept_appointments', 'reject_appointments']

    def accept_appointments(self, request, queryset):
        for appointment in queryset:
            appointment.status = 'Approved'
            appointment.approved = True
            appointment.save()
            self.send_approval_email(appointment)
    accept_appointments.short_description = "Одобрить выбранные заявки"

    def reject_appointments(self, request, queryset):
        for appointment in queryset:
            appointment.status = 'Rejected'
            appointment.approved = False
            appointment.save()
            self.send_rejection_email(appointment)
    reject_appointments.short_description = "Отклонить выбранные заявки"


    def send_approval_email(self, appointment):
        subject = "Ваша заявка одобрена"
        message = f"""
        Здравствуйте {appointment.full_name},
        Ваша заявка на прием по услуге "{appointment.service}" на {appointment.appointment_date} в {appointment.appointment_time} одобрена.
        """
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = appointment.email
        send_mail(subject, message, from_email, [to_email], fail_silently=False)

    def send_rejection_email(self, appointment):
        subject = "Ваша заявка отклонена"
        message = f"""
        Здравствуйте {appointment.full_name},
        Ваша заявка на прием по услуге "{appointment.service}" на {appointment.appointment_date} в {appointment.appointment_time} отклонена.
        """
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = appointment.email
        send_mail(subject, message, from_email, [to_email], fail_silently=False)

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
            self.send_response_email(request, obj)
        super().save_model(request, obj, form, change)

    def send_response_email(self, request, obj):
        subject = "Ответ на ваш вопрос"
        message = f"Спасибо за ваше обращение {obj.full_name}, я ответила на ваш вопрос:\n\n{obj.message}\n\nОтвет:\n{obj.response}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = obj.email
        send_mail(subject, message, from_email, [to_email], fail_silently=False)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'created_at', 'updated_at')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Testimonial)