from django.contrib import admin
from django.urls import path,include
from administrator import views


urlpatterns = [
    path("admin_login/",views.admin_login, name='login'),
    path("dashboard/", views.dashboard, name="dashboard"),
    # path("dashboard", views.dashboard, name="dashboard")

    path("dashboard/",views.dashboard, name='dashboard'),

    path("product/", views.product, name='product'),

    path('customer/', views.customer, name='customer'),

    path('order/', views.order, name='order'),

]
