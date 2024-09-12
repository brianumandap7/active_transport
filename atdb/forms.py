from django import forms
from .models import Typeofwork

class TypeofworkForm(forms.ModelForm):
    class Meta:
        model = Typeofwork
        fields = ['Typeofwork']
