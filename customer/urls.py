from django.contrib import admin
from django.urls import path,include
from customer import views

urlpatterns = [

    path('', views.home, name='home'),

    path("register/",views.register, name='register'),

    path("login/", views.login, name='login'),

    path('homepage/', views.homepage, name='homepage'),

    path('contact/', views.contact, name='contact'),

]