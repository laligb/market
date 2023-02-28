from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.CharField(max_length=30, default='retailer')

    def __str__(self):
        return f'{self.first_name[0].capitalize()}.{self.last_name.capitalize()}'
