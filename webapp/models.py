from django.db import models

# Create your models here.
class SignupDB(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)
    email=models.CharField(max_length=20,blank=True,null=True)
    password=models.CharField(max_length=20,blank=True,null=True)
    confirmpass=models.CharField(max_length=20,blank=True,null=True)

