from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class UserDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user_name


class Contact(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    comment = models.TextField(max_length=999)
    email = models.EmailField(blank=False)

    class Meta:
        db_table = "contactus"

