from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.
def home( request):
    return render(request, 'home.html',{})

class AboutUsView(ListView):
    template_name = 'AboutUs.html'

    def get_queryset(self):
        return None


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'Register.html'

    def get_success_url(self):
        return reverse_lazy('Massege')


class MassegeView(ListView):
    template_name = 'Massege.html'

    def get_queryset(self):
        return None