from django.shortcuts import render, HttpResponse
from django.urls.conf import include


def index_page(request):
    return render(request, "index.html")


def register_page(request):
    return render(request, "Register/register.html")


def login_page(request):
    return render(request, "login.html")

def about_page(request):
    return render(request, "aboutUs/aboutus.html")