from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Appointment
from .forms import ContactForm, AppointmentForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка формы обратной связи
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender_email = form.cleaned_data['email']
            recipient_list = [settings.ADMIN_EMAIL]  # Замените на вашу почту администратора
            send_mail(subject, message, sender_email, recipient_list)
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})

def services(request):
    services = Service.objects.all()
    appointment_form = AppointmentForm()

    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment_date = appointment_form.cleaned_data['appointment_date']
            appointment_time = appointment_form.cleaned_data['appointment_time']
            if not Appointment.objects.filter(appointment_date=appointment_date, appointment_time=appointment_time).exists():
                appointment = appointment_form.save(commit=False)
                appointment.save()
                subject = "Новая запись на прием"
                message = f"Новая запись на прием:\nДата: {appointment_date}\nВремя: {appointment_time}"
                sender_email = appointment.email
                recipient_list = [settings.ADMIN_EMAIL]
                send_mail(subject, message, sender_email, recipient_list, fail_silently=False)
                return redirect('success')
            else:
                appointment_form.add_error(None, "Это время уже занято, выберите другое.")

    return render(request, 'services.html', {'services': services, 'appointment_form': appointment_form})

def appointment(request):
    appointment_form = AppointmentForm()
    return render(request, 'appointment.html', {'appointment_form': appointment_form})

def appointment_submit(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.save()
            subject = "Новая запись на прием"
            message = f"Новая запись на прием:\nДата: {appointment.appointment_date}\nВремя: {appointment.appointment_time}"
            sender_email = appointment.email
            recipient_list = [settings.ADMIN_EMAIL]
            send_mail(subject, message, sender_email, recipient_list, fail_silently=False)
            return redirect('success')
    return redirect('services')

def admin_panel(request):
    if request.method == 'POST':
        # Логика принятия или отклонения заявки
        appointment_id = request.POST.get('appointment_id')
        action = request.POST.get('action')
        if action == 'accept':
            appointment = Appointment.objects.get(pk=appointment_id)
            appointment.accepted = True
            appointment.save()
            # Отправка письма клиенту об успешном подтверждении записи
            subject = "Запись на прием подтверждена"
            message = "Ваша запись на прием подтверждена."
            recipient_list = [appointment.email]
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
        elif action == 'reject':
            appointment = Appointment.objects.get(pk=appointment_id)
            appointment.delete()  # Удаление записи
            # Отправка письма клиенту об отклонении записи
            subject = "Запись на прием отклонена"
            message = "Ваша запись на прием отклонена."
            recipient_list = [appointment.email]
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
    appointments = Appointment.objects.all()
    return render(request, 'admin_panel.html', {'appointments': appointments})

def success(request):
    return render(request, 'success.html')

def contacts(request):
    # Add your logic for the contacts view here
    return render(request, 'contacts.html')  # Assuming you have a template named 'contacts.html'

def about(request):
    # Добавьте вашу логику для страницы "О нас" здесь
    return render(request, 'about.html')  # Предполагается, что у вас есть шаблон с именем 'about.html'

def appointment(request):
    # Добавьте вашу логику для страницы записи на прием здесь
    return render(request, 'appointment.html')  # Предполагается, что у вас есть шаблон с именем 'appointment.html'

def article1(request):
    # Fetch the article with slug 'article1'
    article = Article.objects.get(slug='article1')
    return render(request, 'article1.html', {'article': article})

def article2(request):
    # Fetch the article with slug 'article2'
    article = Article.objects.get(slug='article2')
    return render(request, 'article2.html', {'article': article})
def article3(request):
    # Fetch the article with slug 'article2'
    article = Article.objects.get(slug='article3')
    return render(request, 'article3.html', {'article': article})
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'article_detail.html', {'article': article})
def article4(request):
    # Fetch the article with slug 'article1'
    article = Article.objects.get(slug='article4')
    return render(request, 'article4.html', {'article': article})

def article5(request):
    # Fetch the article with slug 'article2'
    article = Article.objects.get(slug='article5')
    return render(request, 'article5.html', {'article': article})

def article6(request):
    # Fetch the article with slug 'article2'
    article = Article.objects.get(slug='article6')
    return render(request, 'article6.html', {'article': article})

def article7(request):
    # Fetch the article with slug 'article2'
    article = Article.objects.get(slug='article7')
    return render(request, 'article7.html', {'article': article})
def article8(request):
    # Fetch the article with slug 'article2'
    article = Article.objects.get(slug='article8')
    return render(request, 'article8.html', {'article': article})
def article9(request):
    # Fetch the article with slug 'article2'
    article = Article.objects.get(slug='article9')
    return render(request, 'article9.html', {'article': article})
def article10(request):
    # Fetch the article with slug 'article2'
    article = Article.objects.get(slug='article10')
    return render(request, 'article10.html', {'article': article})

def privacy_policy(request):
    return render(request, 'privacy_policy.html')