from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

        widgets = {
            'Customer': forms.TextInput(attrs={'class': 'form-control'}),
            'Date': forms.DateInput(attrs={'class': 'form-control'}),
            'Time': forms.TimeInput(attrs={'class': 'form-control'}),
            'Period': forms.TextInput(attrs={'class': 'form-control'}),
            'Location': forms.TextInput(attrs={'class': 'form-control'}),
        }

