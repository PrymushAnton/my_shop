from django.db import models

# Create your models here.
class Data(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.IntegerField()