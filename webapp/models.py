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
    productname=models.CharField(max_length=30,blank=True,null=True)
    productprice=models.IntegerField(blank=True,null=True)
    username=models.CharField(max_length=20,blank=True,null=True)
    productimage=models.ImageField(upload_to='product_images',null=True,blank=True)

class CheckoutDB(models.Model):
    fname=models.CharField(max_length=20,blank=True,null=True)
    lname=models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField(max_length=20,blank=True,null=True)
    address=models.TextField(max_length=20,blank=True,null=True)
    city=models.CharField(max_length=20,blank=True,null=True)
    state=models.CharField(max_length=20,blank=True,null=True)
    pin=models.CharField(max_length=20,blank=True,null=True)
    total=models.IntegerField(blank=True,null=True)



