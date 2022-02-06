from os import name
from django.contrib import admin
from django.urls import path, include
from products import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

app_name = "products"
urlpatterns = [
    path("", views.index_page, name="Home"),
    path("register_page/", views.register_page, name="register"),
    path("login_page/", views.login_page, name="login"),
    path("aboutus_page/",views.about_page, name="about"),
]