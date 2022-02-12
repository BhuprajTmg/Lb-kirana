from django import forms

from .models import *

class productdetails(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('__all__')