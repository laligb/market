from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    quantity = models.IntegerField()
