from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField(max_length=100)
    image_url = models.CharField(max_length=5000, null=True, blank=True)
    category = models.CharField(max_length=12)

    def __str__(self):
        return str(self.name)


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=24, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)
