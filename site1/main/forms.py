from django import forms
from .models import Appointment
from datetime import date
from .models import Question
class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['full_name', 'email', 'appointment_date', 'appointment_time', 'service']

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data['appointment_date']
        if appointment_date < date.today():
            raise forms.ValidationError("Вы не можете выбрать дату, которая уже прошла.")
        return appointment_date



