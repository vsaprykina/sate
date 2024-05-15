from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='Описание услуги')
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/img/', default='services/img/default.jpg')

class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='articles/images/')


