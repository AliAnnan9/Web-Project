from django.db import models
from Cars.models import Car

# Create your models here.
class Appointment(models.Model):
    Customer=models.CharField(max_length=255,null=True)
    Date = models.DateField(null=True)
    Time = models.TimeField(null=True)
    Period = models.CharField(max_length=50)
    Location=models.CharField(max_length=255,null=True)

    def __str__(self) -> str:
        return self.Customer + ' ' + str(self.Date )