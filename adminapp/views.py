from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from adminapp.models import CategoryDB, ProductDB


# Create your views here.
def index(request):
    categories=CategoryDB.objects.count()
    products=ProductDB.objects.count()
    date=datetime.datetime.now()
    return render(request,'index.html',{'date':date,'categories':categories,'products':products})
def add_category(request):
    return render(request,'add_category.html')
def save_category(request):
    if request.method=='POST':
        n=request.POST.get('name')
        d=request.POST.get('desc')
        obj=CategoryDB(name=n,description=d)
        obj.save()
    return redirect(add_category)
def display_category(request):
    data=CategoryDB.objects.all()
    return render(request,'display_category.html',{'data':data})
def edit_category(request,cid):
    data=CategoryDB.objects.get(id=cid)
    return render(request,'edit_category.html',{'data':data})
def update_category(request,cid):
    if request.method=='POST':
        n=request.POST.get('name')
        d=request.POST.get('desc')
        CategoryDB.objects.filter(id=cid).update(name=n,description=d)
    return redirect(display_category)
def delete_category(request,cid):
    data=CategoryDB.objects.get(id=cid)
    data.delete()
    return redirect(display_category)

def add_product(request):
    data=CategoryDB.objects.all()
    return render(request,'add_product.html',{'data':data})
def save_product(request):
    if request.method=='POST':
        n=request.POST.get('name')
        p=request.POST.get('price')
        d=request.POST.get('desc')
        m=request.POST.get('manufacturer')
        c=request.POST.get('category')
        i=request.FILES['image']
        obj=ProductDB(name=n,price=p,description=d,manufacturer=m,image=i,category=c)
        obj.save()
    return redirect(add_product)
def display_product(request):
    data=ProductDB.objects.all()
    return render(request,'display_product.html',{'data':data})
def edit_product(request,pid):
    data=ProductDB.objects.get(id=pid)
    categories=CategoryDB.objects.all()
    return render(request,'edit_product.html',{'data':data,'categories':categories})
def update_product(request,pid):
    if request.method=='POST':
        n=request.POST.get('name')
        p=request.POST.get('price')
        d=request.POST.get('desc')
        m=request.POST.get('manufacturer')
        c=request.POST.get('category')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=ProductDB.objects.get(id=pid).image
        ProductDB.objects.filter(id=pid).update(name=n,price=p,description=d,manufacturer=m,image=file,category=c)
    return redirect(display_product)
def delete_product(request,pid):
    data=ProductDB.objects.get(id=pid)
    data.delete()
    return redirect(display_product)
def login_page(request):
    return render(request,'login.html')

def admin_login(request):
    if request.method=='POST':
        u=request.POST.get('username')
        p=request.POST.get('pass')
        if User.objects.filter(username__contains=u).exists():
            data=authenticate(username=u,password=p)
            if data is not None:
                login(request,data)
                request.session['username']=u
                request.session['password']=p
                return redirect(index)
            else:
                return redirect(login_page)
        else:
            return redirect(login_page)

def singlepage(request,pid):
    product=ProductDB.objects.all(id=pid)
    return render(request,'single_product.html')





