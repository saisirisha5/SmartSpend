import uuid
from django.shortcuts import redirect
from .models import Product
from django.http import HttpResponse
import random
from django.shortcuts import render
from django.core.mail import send_mail


def customerhomepage(request):
    # Retrieve random products from the database
    products = Product.objects.all()
    random_products = random.sample(list(products), min(len(products), 51))  # Get 3 random products

    return render(request, 'customer/customerhomepage.html', {'random_products': random_products})


def categories(request):
    return render(request,'customer/categories.html')


def homeaccessories(request):
    home = Product.objects.filter(id__range=(25, 32))
    return render(request, 'customer/homeaccesories.html' , {'home': home})


# views.py
def mobiles(request):
    # Retrieve products with IDs ranging from 1 to 22 and sort them by price
    mobile = Product.objects.filter(id__range=(1, 24))

    return render(request, 'customer/mobiles.html', {'mobile': mobile})

def shirts(request):
    shirt = Product.objects.filter(id__range=(33, 42))

    return render(request, 'customer/shirts.html', {'shirt': shirt})

def babycare(request):
    baby=Product.objects.filter(id__range=(43, 78))

    return render(request,'customer/babycare.html',{'baby':baby})

def women(request):
    fashion=Product.objects.filter(id__range=(79,103))

    return render(request,'customer/women.html',{'fashion':fashion})

def contact(request):
     if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        message = f"Name: {firstname} {lastname}\nEmail: {email}\nComment: {comment}"
        send_mail(
            'New Contact Form Submission',
            message,
            email,  # from email
            ['prabhalasaisirisha25@gmail.com'],  # to email
        )
        return render(request,'customer/contact.html')
     return render(request,'customer/contact.html')


def search_product(request):
    query = request.GET.get('q')
    results = []

    if query:
        # Filter products by name containing the query
        results = Product.objects.filter(name__icontains=query)
        # Sort the filtered results by price in ascending order
        results = results.order_by('price')

    return render(request, 'customer/search_product.html', {'results': results})
