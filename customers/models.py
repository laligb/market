from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import validate_email

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.CharField(max_length=30, default='retailer')

    def __str__(self):
        return f'{self.first_name[0].capitalize()}.{self.last_name.capitalize()}'


# CustomerModel
def validate_customers(value):
    """
    Validator function to ensure that the birth date is not in the future.
    """
    if value > timezone.now().date():
        raise ValidationError('Birth date cannot be in the future.')


class CustomerModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(validators=[validate_customers])
    is_active = models.BooleanField(default=True)
    email = models.EmailField(validators=[validate_email])

    def __str__(self):
        return f'{self.first_name[0].capitalize()}.{self.last_name.capitalize()}.{self.birth_date}'
