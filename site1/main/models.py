from django.db import models
from django.utils.text import slugify
class Service(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/img/', default='services/img/default.jpg')


class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    service = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"{self.full_name} - {self.appointment_date} {self.appointment_time}"



class Question(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО', blank=False, null=False)
    email = models.EmailField()
    message = models.TextField()
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Testimonial(models.Model):
    text = models.TextField(verbose_name='Текст отзыва')
    author = models.CharField(max_length=100, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

