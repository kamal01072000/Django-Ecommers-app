from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    pro = product.objects.filter(trending=1)
    return render(request,'eapp/index.html',{'prod':pro})

def register(request):
    form = customuserform() 
    if request.method =='POST': 
        form=customuserform(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request,'Registration Succesful! login Now')
            return redirect('login')
    return render(request,'eapp/register.html',{'form':form})

def login_page(request):
    if request.method =='POST':
        name= request.POST.get('username')
        pwd= request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Login SuccessFully")
            return redirect("home")
        else: 
            messages.error(request,"invalid username or Password")
            return redirect('login')
    return render (request,'eapp/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logout successfully')
    return redirect("home")

def products(request):
    ctg = catogery.objects.filter(status=0)
    return render(request,'eapp/products.html',{'catogery':ctg})

def collection_view(request,name):
    if(catogery.objects.filter(name=name,status=0)):
        products= product.objects.filter(catogery__name=name)
        return render(request,'eapp/collections.html',{'prod':products,'collc_name':name})
    else:
        messages.warning(request,"no such product")
        return redirect('products')

def collection_detailes(request ,cname,pname):
    if(catogery.objects.filter(name=cname,status=0)):
        if(product.objects.filter(name=pname,status=0)):
            det= product.objects.filter(name=pname,status=0).first()
            return render(request,'eapp/collectionsdetailes.html',{'collc_det':det})
        else:
            messages.warning(request,"no such product")
            return redirect('products')
    else:
        messages.warning(request,"no such product")
        return redirect('products')
