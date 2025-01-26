from django.urls import path
from . import views

urlpatterns = [

     path('', views.customerhomepage, name='customerhomepage'),
     path('categories', views.categories, name='categories'),
     path('homeaccessories', views.homeaccessories, name='homeaccessories'),
     path('mobiles', views.mobiles, name='mobiles'),
     path('shirts', views.shirts, name='shirts'),
     path('babycare',views.babycare,name='babycare'),
     path('women',views.women,name='women'),
     path('contact', views.contact, name='contact'),
     path('search_product', views.search_product, name='search_product'),

]