import email
from itertools import product
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth import  authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import *
from .models import *
from customer.models import *
from products.models import *
from django.contrib import auth
from django.http import Http404



# Create your views here.

def home(request):
    product = Products.objects.all()
    return render(request, 'index.html',{'product':product})

def register(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("here")
            return redirect('/login')

        
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def demo(request):
    return render(request, 'header/base.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
            
        user = Customer.objects.get(email=email, password=password)

        if user is not None:
            return redirect('demo')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/login')
    else:  
        return render(request, 'login.html') 

    


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email'] 
        message =request.POST['message']

        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            # settings.EMAIL_HOST_USER,
            #           ['riyastha406@mail.com'],
            ['bhupraj875@gmail.comm' ], #To email
            # fail_silently= True,
        )   
        return render(request, 'pages/contact.html', {'message_name': message_name}) 

    else:
        return render(request, 'pages/contact.html' , {})

def contact_log(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email'] 
        message =request.POST['message']

        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            # settings.EMAIL_HOST_USER,
            #           ['riyastha406@mail.com'],
            ['bhupraj875@gmail.comm' ], #To email
            # fail_silently= True,
        )   
        return render(request, 'header/contact.html', {'message_name': message_name}) 

    else:
        return render(request, 'header/contact.html' , {})
# Auth.login is a default login function given by django.  which checks the data from database and the users given input

def products(request):
    product = Products.objects.all()
    return render(request, 'index.html')

def deleteproduct(request, product_id):
    customer = Customer.objects.get(product_id=product_id)
    customer.delete()
    return redirect ('Admin/home')