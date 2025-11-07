from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    description=models.TextField(max_length=200,null=True,blank=True)

class ProductDB(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    manufacturer=models.CharField(max_length=20,null=True,blank=True)
    category=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField(upload_to="productimage",null=True,blank=True)