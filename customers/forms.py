from django import forms
from .models import CustomerModel

class CustomerForm(forms.ModelForm):
    #name = forms.CharField()

    class Meta:
        model=CustomerModel
        fields='__all__'
