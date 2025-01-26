from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails, Contact
from django.contrib import messages,auth
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import IntegrityError
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserDetails


def homepage(request):
    return render(request,'project/homepage.html')


def about(request):
    return render(request,'project/about.html')


def shopnow(request):
    return render(request,'project/shopnow.html')



def contact(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        comment = request.POST['comment']
        email = request.POST['email']
        subject = "If you have any query regarding SmartSpend"
        comment1 = comment + " This is a system-generated mail. Please do not respond."

        data = Contact(firstname=firstname, lastname=lastname, comment=comment, email=email)
        data.save()
        send_mail(
            subject,
            comment1,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        # Return JSON response indicating success
        return JsonResponse({'message': 'Mail Sent Successfully'}, status=200)
    return render(request, "project/contact.html")




# def signup(request):
#     if request.method == 'POST':
#         try:
#             first_name = request.POST.get('first_name')
#             last_name = request.POST.get('last_name')
#             user_name = request.POST.get('user_name')
#             password1 = request.POST.get('password1')
#             password2 = request.POST.get('password2')
#             email = request.POST.get('email')
#             phone = request.POST.get('phone')
#             gender = request.POST.get('gender')
#             profile_picture = request.FILES.get('image')
#
#             if password1 != password2:
#                 messages.error(request, "Passwords do not match.")
#                 return redirect('signup')
#
#             user = UserDetails.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 user_name=user_name,
#                 password=password1,
#                 email=email,
#                 phone=phone,
#                 gender=gender,
#                 profile_picture=profile_picture,
#             )
#             user.save()
#             return redirect('customerlogin')
#
#         except IntegrityError:
#             # Handle IntegrityError (missing required fields)
#             error_message = "Please fill all the required information."
#             return render(request, 'project/signup.html', {'error': error_message})
#
#     return render(request, 'project/signup.html')

def signup(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        profile_picture = request.FILES.get('image')

        # Check for empty fields
        if not all([first_name, last_name, user_name, password1, password2, email, phone, gender, profile_picture]):
            error_message = "Please fill all the required information."
            return render(request, 'project/signup.html', {'error': error_message})

        # Check if passwords match
        if password1 != password2:
            error_message = "Passwords do not match."
            return render(request, 'project/signup.html', {'error': error_message})

        # Create the user
        try:
            user = UserDetails.objects.create(
                first_name=first_name,
                last_name=last_name,
                user_name=user_name,
                password=password1,
                email=email,
                phone=phone,
                gender=gender,
                profile_picture=profile_picture,
            )
            user.save()
            return redirect('customerlogin')
        except IntegrityError:
            # Handle IntegrityError
            error_message = "An error occurred while creating the user. Please try again later."
            return render(request, 'project/signup.html', {'error': error_message})

    # If GET request or form is not valid, render the signup page
    return render(request, 'project/signup.html')

def adminhomepage(request):
            return render(request, 'adminhomepage.html')


def customerhomepage(request):
            return render(request, 'customerhomepage.html')


def customer_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        try:
            user = UserDetails.objects.get(user_name=user_name)
        except UserDetails.DoesNotExist:
            return render(request, 'project/customer_login.html', {'error': 'Invalid username or password'})

        if user.password != password:
            return render(request, 'project/customer_login.html', {'error': 'Invalid password or username'})
        request.session['user_id'] = user.id
        request.session['user_name'] = user.user_name
        return redirect('customerhomepage')

    # Pass the error variable to the context even for GET requests
    return render(request, 'project/customer_login.html', {'error': ''})

# from django.contrib.auth.hashers import make_password
#
# def forgot_password(request):
#     if request.method == 'POST':
#         username = request.POST.get('user_name')
#         new_password = request.POST.get('new_password')
#
#         # Check if the username exists in the database
#         try:
#             user = UserDetails.objects.get(user_name=username)
#         except UserDetails.DoesNotExist:
#             return render(request, 'project/forgot_password.html', {'error': 'Invalid username'})
#
#         # Update the password
#         user.password = make_password(new_password)  # Manually hash the password
#         user.save()
#         return redirect('customerlogin')  # Redirect to login page after password reset
#
#     return render(request, 'project/forgot_password.html')


from django.contrib.auth.hashers import make_password
import logging

logger = logging.getLogger(__name__)

def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        new_password = request.POST.get('new_password')

        logger.debug(f"Username: {username}, New Password: {new_password}")

        # Check if the username exists in the database
        try:
            user = UserDetails.objects.get(user_name=username)
            logger.debug(f"User found: {user}")
        except UserDetails.DoesNotExist:
            logger.error("User does not exist")
            return render(request, 'project/forgot_password.html', {'error': 'Invalid username'})

        # Manually hash the new password
        hashed_password = make_password(new_password)
        logger.debug(f"Hashed password: {hashed_password}")

        # Update the password
        user.password = hashed_password
        user.save()
        logger.debug("Password updated successfully")
        return redirect('customerlogin')  # Redirect to login page after password reset

    return render(request, 'project/forgot_password.html')
