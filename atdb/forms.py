from django import forms
from .models import Typeofwork, Region

class TypeofworkForm(forms.ModelForm):
    class Meta:
        model = Typeofwork
        fields = ['Typeofwork']
        widgets = {
            'Typeofwork': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'Typeofwork': '',  # Remove the label
        }

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['Region']
        widgets = {
            'Region': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'Region': '',  # Remove the label
        }