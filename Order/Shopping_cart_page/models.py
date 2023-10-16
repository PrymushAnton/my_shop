from django.db import models

# Create your models here.

# class Product(models.Model):
#     pass

class Cart(models.Model):
    user = models.CharField(max_length=255)
    # product_list = models.ManyToManyField(Product, blank=True, null=True)
