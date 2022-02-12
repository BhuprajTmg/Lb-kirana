from django import forms

from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('__all__')