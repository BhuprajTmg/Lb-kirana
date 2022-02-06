
from django.shortcuts import redirect, render
from django.contrib.auth import  authenticate,login
from django.contrib.auth.models import User

# Create your views here.

def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        admin = authenticate(request, username=username, password=password)
        print(admin)
        if admin is not None:
            login(request, admin)
            return redirect('/admin/dashboard')
        
        else:
            return redirect('/admin/admin_login')
    return render(request, "Admin/login.html")


def dashboard(request):
    return render(request,'Admin/dashboard.html')

# def login():
#     return render(request,'/Admin/login.html')

def product(request):
    return render(request, 'Admin/products.html')

def customer(request):
    return render(request, 'Admin/customer.html')

def order(request):
    return render(request, 'Admin/order.html')
