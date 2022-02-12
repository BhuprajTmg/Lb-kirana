
from cmath import e
from email import message
from django.shortcuts import redirect, render
from django.contrib.auth import  authenticate,login
from django.contrib.auth.models import User
from customer.models import *
from products.forms import productdetails
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

def myprofile(request):
    users = Customer.objects.all()
    return render(request,'Admin/myprofile.html',{'users':users})

# def login():
#     return render(request,'/Admin/login.html')

def product(request):
    if request.method =='POST':
        form = productdetails(request.POST)
        if form.is_valid():
            form.save()
            print("here")
            return redirect('/')
        else:
            print(form) 
            return redirect('/admin/product')
    return render(request, 'Admin/products.html')

def customer(request):
    users = Customer.objects.all()
    return render(request, 'Admin/customer.html',{'users':users})

def order(request):
    return render(request, 'Admin/order.html')

def ForgetPassword(request):
    try:
        if request.method=='POST':
            username = request.POST.get('username')

            if not User.objects.filter(username=username).first():
                message.success(request,'Not user found with this user name')
                return redirect('/ForgetPassword/')

            user_obj = User.objects.get(username=username)
        

    except Exception as e:
        print(e)

    return render(request, 'Admin/forget-password.html')
