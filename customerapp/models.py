from django.db import models

# Create your models here.
# In products/models.py
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    review = models.TextField()
    website = models.TextField()
    buy = models.TextField()

    def __str__(self):
        return self.name
