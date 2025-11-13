from tkinter.font import names

from django.shortcuts import render,redirect
from unicodedata import category

from adminapp.models import CategoryDB,ProductDB
from webapp.models import SignupDB, MessageDB


# Create your views here.
def home(request):
    categories=CategoryDB.objects.all()
    products=ProductDB.objects.all()
    return render(request,'home.html',{'categories':categories,'products':products})
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

def sign_in(request):
    return render(request,'sign_in.html')

def sign_up(request):
    return render(request,'sign_up.html')

def singlepage(request,pid):
    product=ProductDB.objects.get(id=pid)
    categories=CategoryDB.objects.all()
    return render(request,'single_product.html',{'product':product,'categories':categories})

def save_signup(request):
    if request.method=='POST':
        n=request.POST.get('uname')
        e=request.POST.get('email')
        p=request.POST.get('password')
        c=request.POST.get('confirmpass')
        obj=SignupDB(name=n,email=e,password=p,confirmpass=c)
        if SignupDB.objects.filter(name=n).exists():
            return redirect(sign_up)
        elif SignupDB.objects.filter(email=e):
            return redirect(sign_up)
        else:
            obj.save()
            return redirect(sign_in)
def user_login(request):
    if request.method=='POST':
        n=request.POST.get('username')
        p=request.POST.get('password')
        if SignupDB.objects.filter(name=n,password=p).exists() :
            request.session['name']=n
            request.session['password']=p
            return redirect(home)
        else:
            return redirect(sign_in)
    else:
        return redirect(sign_in)
def user_logout(request):
    del request.session['name']
    del request.session['password']
    return redirect(sign_in)
def save_message(request):
    if request.method=='POST':
        n=request.POST.get('name')
        m=request.POST.get('email')
        message=request.POST.get('message')
        obj=MessageDB(name=n,email=m,message=message)
        obj.save()
    return redirect(contact)


