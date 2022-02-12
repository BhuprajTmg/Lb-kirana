from django.contrib import admin
from django.urls import path, include
from products import views

app_name = "products"
urlpatterns = [
    path("", views.index_page, name="Home"),
    path("register_page/", views.register_page, name="register"),
    path("login_page/", views.login_page, name="login"),
    path("aboutus_page/",views.about_page, name="about"),
    path("about_log/",views.about_log, name="about"),
    path("index_log/",views.index_log, name="index"),
    path("faqs/",views.faqs, name="faqs"),
    path("terms/",views.terms, name="terms"),
    path("help/",views.help, name="help"),

]