from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Appointment, Article
from .forms import ContactForm, AppointmentForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

def index(request):
    return render(request, 'index.html')

def services(request):
    services = Service.objects.all()
    appointment_form = AppointmentForm()

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
            return redirect('services')

    return render(request, 'services.html', {'services': services, 'appointment_form': appointment_form})

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
def article1(request):
    return render(request, 'article1.html')

def article2(request):
    return render(request, 'article2.html')

def article3(request):
    return render(request, 'article3.html')

def article4(request):
    return render(request, 'article4.html')

def article5(request):
    return render(request, 'article5.html')

def article6(request):
    return render(request, 'article6.html')

def article7(request):
    return render(request, 'article7.html')

def article8(request):
    return render(request, 'article8.html')

def article9(request):
    return render(request, 'article9.html')
def article10(request):
    return render(request, 'article10.html')
def privacy_policy(request):
    return render(request, 'privacy_policy.html')
def appointment_submit(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлена.')
            return redirect('services')
        else:
            messages.error(request, 'Ошибка в отправке заявки. Пожалуйста, попробуйте снова.')
            return redirect('services')
    else:
        return redirect('services')