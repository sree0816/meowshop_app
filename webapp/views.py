

from django.shortcuts import render,redirect


from adminapp.models import CategoryDB,ProductDB
from webapp.models import SignupDB, MessageDB, CartDB


# Create your views here.
def home(request):
    categories=CategoryDB.objects.all()
    products=ProductDB.objects.all()
    categories = CategoryDB.objects.all()
    data = CartDB.objects.filter(username=request.session['name'])
    cart_total = 0
    uname = request.session.get('name')
    if uname:
        cart_total = CartDB.objects.filter(username=uname).count()
    return render(request,'home.html',{'categories':categories,'products':products,'cart_total':cart_total})

def about(request):
    categories = CategoryDB.objects.all()
    data = CartDB.objects.filter(username=request.session['name'])
    cart_total = 0
    uname = request.session.get('name')
    if uname:
        cart_total = CartDB.objects.filter(username=uname).count()
    categories=CategoryDB.objects.all()
    return render(request,'about.html',{'categories':categories,'cart_total':cart_total})

def contact(request):
    categories = CategoryDB.objects.all()
    data = CartDB.objects.filter(username=request.session['name'])
    cart_total = 0
    uname = request.session.get('name')
    if uname:
        cart_total = CartDB.objects.filter(username=uname).count()
    categories=CategoryDB.objects.all()
    return render(request,'contact.html',{'categories':categories,"cart_total":cart_total})

def shop(request):
    categories=CategoryDB.objects.all()
    product=ProductDB.objects.all()
    categories = CategoryDB.objects.all()
    data = CartDB.objects.filter(username=request.session['name'])
    cart_total = 0
    uname = request.session.get('name')
    if uname:
        cart_total = CartDB.objects.filter(username=uname).count()
    return render(request,'shop.html',{'categories':categories,'product':product,'cart_total':cart_total})

def filtered(request,cat):
    categories = CategoryDB.objects.all()
    data = CartDB.objects.filter(username=request.session['name'])
    cart_total = 0
    uname = request.session.get('name')
    if uname:
        cart_total = CartDB.objects.filter(username=uname).count()
    product=ProductDB.objects.filter(category=cat)
    categories=CategoryDB.objects.all()
    return render(request,'filtered.html',{'product':product,'categories':categories,'cart_total':cart_total})

def sign_in(request):
    return render(request,'sign_in.html')

def sign_up(request):
    return render(request,'sign_up.html')

def singlepage(request,pid):
    categories = CategoryDB.objects.all()
    data = CartDB.objects.filter(username=request.session['name'])
    cart_total = 0
    uname = request.session.get('name')
    if uname:
        cart_total = CartDB.objects.filter(username=uname).count()
    product=ProductDB.objects.get(id=pid)
    categories=CategoryDB.objects.all()
    return render(request,'single_product.html',{'product':product,'categories':categories,'cart_total':cart_total})

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
    if 'name' in request.session:
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

def cart(request):
    #filtering books based on users

    categories = CategoryDB.objects.all()
    data=CartDB.objects.filter(username=request.session['name'])
    cart_total=0
    uname=request.session.get('name')
    if uname:
        cart_total=CartDB.objects.filter(username=uname).count()

    #calulating total amount
    sub_total=0
    del_charge=0
    total_amount=0

    #iteraring through products added by user
    for i in data:
        sub_total += i.totalprice
        if sub_total>500 and sub_total<1000:
            del_charge=50
        elif sub_total>1000:
            del_charge=0
        else:
            del_charge=100

        total_amount=sub_total+del_charge
    return render(request,'cart.html',{'categories':categories,'cart_total':cart_total,'data':data,'sub_total':sub_total,'del_charge':del_charge,'total_amount':total_amount})

def checkout(request):
    return render(request,'checkout.html')

def save_cart(request):
    if request.method=='POST':
        name=request.POST.get('productname')
        quantity=int(request.POST.get('quantity'))
        price=int(request.POST.get('price'))
        username=request.POST.get('username')
        tp=request.POST.get('total_price')

        product=ProductDB.objects.filter(name=name).first()
        img=product.image if product else None
        obj=CartDB(quantity=quantity,productname=name,totalprice=tp,productprice=price,username=username,productimage=img)
        obj.save()
        return redirect(cart)
def delete_cart(request,pid):
    pro=CartDB.objects.get(id=pid)
    pro.delete()
    return redirect(cart)
