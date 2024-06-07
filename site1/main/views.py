from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Appointment
from .forms import ContactForm, AppointmentForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from datetime import datetime
from .models import Question
from django.shortcuts import render, get_object_or_404
from .models import Article
from .models import Testimonial


def contact_page(request):
    return render(request, 'contacts.html')

def index(request):
    if request.method == 'POST':
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        agree = request.POST.get('agree')

        if agree:
            Question.objects.create(
                full_name=full_name,
                email=email,
                message=message
            )
            messages.success(request, 'Спасибо за обращение! Я скоро вам отвечу.')
            return redirect('index#contact-form')

    featured_articles = Article.objects.filter(is_featured=True)[:4]
    other_articles = Article.objects.filter(is_featured=False)
    all_articles = Article.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {
        'featured_articles': featured_articles,
        'other_articles': other_articles,
        'all_articles': all_articles,
        'testimonials': testimonials,
    })

def index_question_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        agree = request.POST.get('agree')

        errors = {}
        if not full_name:
            errors['full-name'] = 'Пожалуйста, введите ФИО.'
        if not email:
            errors['email'] = 'Пожалуйста, введите email.'
        if not message or len(message) < 10:
            errors['message'] = 'Пожалуйста, введите сообщение длиной не менее 10 символов.'
        if not agree:
            errors['agree'] = 'Вы должны согласиться с политикой конфиденциальности.'

        if errors:
            for field, error in errors.items():
                messages.error(request, error)
        else:
            question = Question.objects.create(
                full_name=full_name,
                email=email,
                message=message
            )
            messages.success(request, 'Спасибо за обращение! Ответ придет на указнную электронную почту.')

            # Отправка email уведомления
            subject = "Ваш вопрос успешно отправлен"
            email_message = f"""
            Здравствуйте {full_name},

            Ваш вопрос:
            "{message}"

            Спасибо за ваше обращение! Я отвечу вам в ближайшее время.

            С уважением,
            ваш логопед, Елена
            """
            send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)

            return redirect('index')

    return render(request, 'index.html')

def services(request):
    services = Service.objects.all()
    appointment_form = AppointmentForm()
    available_times = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00']

    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save()
            subject = "Новая запись на прием"
            message = f"Новая запись на прием:\n{appointment}"
            sender_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.ADMIN_EMAIL]
            send_mail(subject, message, sender_email, recipient_list)
            messages.success(request, 'Ваша заявка успешно отправлена.')
            return redirect('services#appointment-form')
        else:
            print("Appointment form is not valid")

    return render(request, 'services.html', {'services': services, 'appointment_form': appointment_form, 'available_times': available_times})

@method_decorator(staff_member_required, name='dispatch')
class ServiceListView(ListView):
    model = Service
    template_name = 'admin/service_list.html'
    context_object_name = 'object_list'

@method_decorator(staff_member_required, name='dispatch')
class ServiceCreateView(CreateView):
    model = Service
    fields = '__all__'
    template_name = 'admin/service_form.html'
    success_url = '/admin/services/'

@method_decorator(staff_member_required, name='dispatch')
class ServiceUpdateView(UpdateView):
    model = Service
    fields = '__all__'
    template_name = 'admin/service_form.html'
    success_url = '/admin/services/'

@method_decorator(staff_member_required, name='dispatch')
class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'admin/service_confirm_delete.html'
    success_url = '/admin/services/'

def success(request):
    return render(request, 'success.html')

def appointment(request):
    appointment_form = AppointmentForm()
    return render(request, 'appointment.html', {'appointment_form': appointment_form})

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')

def privacy_policy_view(request):
    return render(request, 'privacy_policy.html')

def appointment_available_times(request, appointment_date):
    approved_appointments = Appointment.objects.filter(appointment_date=appointment_date, approved=True)
    available_times = ['10:00', '10:40', '11:20', '12:00', '12:40', '13:20', '14:00', '14:40', '15:20', '16:00', '16:40', '17:20', '18:00']
    for appointment in approved_appointments:
        available_times.remove(appointment.appointment_time.strftime('%H:%M'))
    return JsonResponse(available_times, safe=False)


def appointment_submit(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        appointment_date = request.POST.get('appointmentDate')
        appointment_time = request.POST.get('appointmentTime')
        service = request.POST.get('service')

        # Проверка, занято ли указанное время
        approved_appointments = Appointment.objects.filter(
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            approved=True
        )
        if approved_appointments.exists():
            messages.error(request, 'Извините, это время уже занято. Пожалуйста, выберите другое время.')
            return redirect('services')

        # Создание новой заявки на прием
        appointment = Appointment(
            full_name=full_name,
            email=email,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            service=service,
            approved=False
        )
        appointment.save()

        # Отправка уведомления пользователю
        subject = "Ваша заявка успешно отправлена"
        message = f"""
        Здравствуйте {full_name},

        Ваша заявка на прием по услуге "{service}" на {appointment_date} в {appointment_time} успешно отправлена. Я свяжусь с вами в ближайшее время для подтверждения.
        """
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)

        messages.success(request, 'Ваша заявка успешно отправлена. Я свяжусь с вами в ближайшее время (ждите ответ на указанную электронную почту).')
        return redirect('services')

    return redirect('services')

def home_page(request):
    featured_articles = Article.objects.filter(is_featured=True)[:4]
    other_articles = Article.objects.filter(is_featured=False)
    return render(request, 'index.html', {
        'featured_articles': featured_articles,
        'other_articles': other_articles,
    })

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {
        'article': article,
    })






def index(request):
    featured_articles = Article.objects.filter(is_featured=True)[:4]
    other_articles = Article.objects.filter(is_featured=False)
    all_articles = Article.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {
        'featured_articles': featured_articles,
        'other_articles': other_articles,
        'all_articles': all_articles,
        'testimonials': testimonials,
    })