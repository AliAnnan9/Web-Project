from django.shortcuts import render
from django.views.generic import ListView,DetailView
from Cars.models import Car 
from .forms import AppointmentForm
from .models import Appointment
# Create your views here.
def home( request):
    return render(request, 'home.html',{})

class FilmDetailView(DetailView):
    model = Car
    template_name = 'Film.html'

def create_Appointment(request , pk):
    cars = Car.objects.get(id = pk)
    form = AppointmentForm()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            cust = form.cleaned_data['Customer']
            date = form.cleaned_data['Date']
            time = form.cleaned_data['Time']
            per = form.cleaned_data['Period']
            loc = form.cleaned_data['Location']
            
            NewAppointment = Appointment(Customer=cust, Date=date, Time=time, Period=per, Location=loc)
            NewAppointment.save()
            return render(request, 'Book.html')

    return render(request, 'Film.html', {'form': form , 'cars' : cars})