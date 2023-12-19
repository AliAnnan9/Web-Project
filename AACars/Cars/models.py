from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    Name=models.CharField(max_length=255)
    Manufactur=models.CharField(max_length=255)
    Model=models.CharField(max_length=255)
    Year=models.CharField(max_length=255)
    Milage=models.CharField(max_length=255)
    Color=models.CharField(max_length=255)
    Engine=models.CharField(max_length=255)
    Power=models.CharField(max_length=255)
    Torque=models.CharField(max_length=255)
    Transmission=models.CharField(max_length=255)
    DriveType=models.CharField(max_length=255)
    Price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='Car_images/',null=True)
    image2=models.ImageField(upload_to='Car_images/',null=True)
    image3=models.ImageField(upload_to='Car_images/',null=True)
    image4=models.ImageField(upload_to='Car_images/',null=True)
    image5=models.ImageField(upload_to='Car_images/',null=True)
    image6=models.ImageField(upload_to='Car_images/',null=True)
    imageHeader=models.ImageField(upload_to='Car_images/',null=True)

    def __str__(self) -> str:
        return self.Manufactur + ' ' + self.Name + ' ' + self.Color