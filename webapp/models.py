from django.db import models

# Create your models here.
class SignupDB(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)
    email=models.CharField(max_length=20,blank=True,null=True)
    password=models.CharField(max_length=20,blank=True,null=True)
    confirmpass=models.CharField(max_length=20,blank=True,null=True)

class MessageDB(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    message=models.CharField(max_length=20,blank=True,null=True)

class CartDB(models.Model):
    quantity=models.IntegerField(blank=True,null=True)
    totalprice=models.IntegerField(blank=True,null=True)
    bookname=models.CharField(max_length=30,blank=True,null=True)
    bookprice=models.IntegerField(blank=True,null=True)
    username=models.CharField(max_length=20,blank=True,null=True)


