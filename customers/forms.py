from django import forms
from .models import CustomerModel
from django.forms import DateInput

class CustomerForm(forms.ModelForm):
    #name = forms.CharField()

    class Meta:
        model=CustomerModel
        fields='__all__'

        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'}),
        }
