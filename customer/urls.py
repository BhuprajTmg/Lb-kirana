from django.contrib import admin
from django.urls import path,include
from customer import views

urlpatterns = [

    path('', views.home, name='home'),

    path("register/",views.register, name='register'),

    path("login/", views.login, name='login'),

    path('contact/', views.contact, name='contact'),

    path('logout/', views.logout, name='logout'),

    path('demo/', views.demo, name='demo'),

    path('contact_log/', views.contact_log, name='contact-log')


]