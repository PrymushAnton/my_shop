from django.db import models

# Create your models here.

# class Product(models.Model):
#     pass

class Cart(models.Model):
    name = models.CharField(max_length=255, default=True)
    image_path = models.CharField(max_length=255, default=True)
    price = models.CharField(max_length=255, default=True)
    # product_list = models.ManyToManyField(Product, blank=True, null=True)
