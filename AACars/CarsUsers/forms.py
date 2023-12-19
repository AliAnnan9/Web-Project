from django import forms
from .models import NormalUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = NormalUser
        fields = '__all__'

        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'UserName': forms.TextInput(attrs={'class': 'form-control'}),
            'FirstName': forms.TextInput(attrs={'class': 'form-control'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control'}),
        }