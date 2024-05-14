from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
