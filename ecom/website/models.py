from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField(max_length=100)
    image_url = models.CharField(max_length=5000, null=True, blank=True)
    category = models.CharField(max_length=12)

    # def __str__(self):
    #     return self.name

    # class Meta:
    #     app_label = 'website'
