"""Django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from app1 import views as views

urlpatterns = [
    path('regex/',views.Employeedata ) ,
    path('admin/', admin.site.urls) ,
    path('app1/',include('app1.urls')) ,
    path('',views.home),
    path('register/',views.register , name = "register") , 
    path('loginPage/',views.loginPage, name = "loginPage") ,
    path('rent_now/',views.rent_now, name="rent_now") ,
    path('logoutUser/',views.logoutUser , name = "logoutUser") ,
    path('invoice/<dic>',views.invoice , name = 'invoice'),
    path('paymentDone/<dic>',views.paymentDone , name = 'paymentDone'),
    path('offers/',views.offer),
    path('about/',views.about,name="about"),
     path('contact/',views.contact,name="contact")
]
