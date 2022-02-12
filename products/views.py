from django.shortcuts import render,redirect
from django.urls.conf import include
from .forms import *
from .models import *

def index_page(request):
    return render(request, "index.html")

def index_log(request):
    return render(request, "header/demo.html")

def register_page(request):
    return render(request, "Register/register.html")

def login_page(request):
    return render(request, "login.html")

def about_page(request):
    return render(request, "aboutUs/aboutus.html")

def faqs(request):
    return render(request, "faqs.html")

def about_log(request):
    return render(request, "header/aboutus.html")

def terms(request):
    return render(request, "terms&condition.html")

def help(request):
    return render(request, "help&support.html")


def addproduct(request):
    if request.method =="POST":
        form = productdetails(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("here")
            return redirect('/')
        else:
            print(form) 

    else:
        return redirect('/admin/product/')
    
    return render(request, 'admin/products.html')
