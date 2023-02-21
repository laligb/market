from django.db import models

# Create your models here.
first_name = models.CharField(max_length=30)
last_name = models.CharField(max_length=30)
status = models.CharField(max_length=30, default='retailer')
