from django.shortcuts import render
from unicodedata import category

from adminapp.models import CategoryDB,ProductDB

# Create your views here.
def home(request):
    categories=CategoryDB.objects.all()
    return render(request,'home.html',{'categories':categories})
def about(request):
    categories=CategoryDB.objects.all()
    return render(request,'about.html',{'categories':categories})

def contact(request):
    categories=CategoryDB.objects.all()
    return render(request,'contact.html',{'categories':categories})
def shop(request):
    categories=CategoryDB.objects.all()
    product=ProductDB.objects.all()
    return render(request,'shop.html',{'categories':categories,'product':product})

def filtered(request,cat):
    product=ProductDB.objects.filter(category=cat)
    categories=CategoryDB.objects.all()
    return render(request,'filtered.html',{'product':product,'categories':categories})