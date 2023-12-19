from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Car
# Create your views here.
def home( request):
    return render(request, 'home.html',{})

def supra( request):
    Car_objects=Car.objects.all()
    return render(request, 'cars.html',{'Car_objects' : Car_objects})

class HomeView(ListView):
    model = Car
    template_name = 'home.html'

class CarDetailView(ListView):
    model = Car
    template_name = 'cars.html'

class VecDetailsView(DetailView):
    model = Car
    template_name = 'List.html'


class BuyView(DetailView):
    model = Car
    template_name = 'Buy.html'
