"""FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from app1 import views
from app1.views import BikeListView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Employeedata,name='home'),
    path('register/', views.register, name="register"),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('rent_now/', views.rent_now, name="rent_now"),
    path('logoutUser/', views.logoutUser, name="logoutUser"),
    path('invoice/<dic>', views.invoice, name='invoice'),
    path('paymentDone/<dic>', views.paymentDone, name='paymentDone'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('bikes/',BikeListView.as_view(),name='bikes')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

