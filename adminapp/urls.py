from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('adminapp/',views.adminhomepage,name='adminhomepage'),
    path('about/', views.about, name='about'),
    path('shopnow', views.shopnow, name='shopnow'),
    path('contact', views.contact, name='contact'),
    path('customer_login/', views.customer_login, name='customerlogin'),
    path('signup', views.signup, name='signup'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
]
