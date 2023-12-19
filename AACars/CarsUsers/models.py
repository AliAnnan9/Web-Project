from django.db import models



# Create your models here.
class NormalUser(models.Model):
    UserName=models.CharField(max_length=255,null=True)
    password=models.CharField(max_length=255,null=True)
    FirstName=models.CharField(max_length=255,null=True)
    LastName=models.CharField(max_length=255,null=True)
    Email=models.CharField(max_length=255,null=True)
    Phone=models.CharField(max_length=15,null=True)
    
    


    def __str__(self) -> str:
        return self.FirstName + ' ' + self.LastName + '/ ' + self.UserName