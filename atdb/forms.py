from django import forms
from .models import Typeofwork, Region, BikeArea, RoadSection, BikeClass, FundSource, bikelanetbl
from django.contrib.auth.forms import PasswordChangeForm

class ExcelUploadForm(forms.Form):
    file = forms.FileField()

class UploadFileForm(forms.Form): #this is for the road section model
    file = forms.FileField()

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

class BikeAreaForm(forms.ModelForm):
    class Meta:
        model = BikeArea
        fields = ['BikeArea']
        widgets = {
            'BikeArea': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'BikeArea': '',  # Remove the label
        }

class RoadSectionForm(forms.ModelForm):
    class Meta:
        model = RoadSection
        fields = ['RoadSection']
        widgets = {
            'RoadSection': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'RoadSection': '',  # Remove the label
        }

class BikeClassForm(forms.ModelForm):
    class Meta:
        model = BikeClass
        fields = ['BikeClass']
        widgets = {
            'BikeClass': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'BikeClass': '',  # Remove the label
        }

class FundSourceForm(forms.ModelForm):
    class Meta:
        model = FundSource
        fields = ['FundSource']
        widgets = {
            'FundSource': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'FundSource': '',  # Remove the label
        }

class BikelaneForm(forms.ModelForm):
    class Meta:
        model = bikelanetbl
        fields = '__all__'  # Include all fields
        widgets = {
            'Bikelane_Code': forms.TextInput(attrs={'class': 'form-control'}),
            'Typeofwork': forms.Select(attrs={'class': 'form-control'}),
            'Region': forms.Select(attrs={'class': 'form-control'}),
            'BikeArea': forms.Select(attrs={'class': 'form-control'}),
            'RoadSection': forms.Select(attrs={'class': 'form-control'}),
            'Length': forms.TextInput(attrs={'class': 'form-control'}),
            'StartPointX': forms.TextInput(attrs={'class': 'form-control'}),
            'StartPointY': forms.TextInput(attrs={'class': 'form-control'}),
            'EndPointX': forms.TextInput(attrs={'class': 'form-control'}),
            'EndPointY': forms.TextInput(attrs={'class': 'form-control'}),
            'BikeClass': forms.Select(attrs={'class': 'form-control'}),
            'BikeDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'FundSource': forms.Select(attrs={'class': 'form-control'}),
            'Remarks': forms.TextInput(attrs={'class': 'form-control'}),
            'Province': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UpdatePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Old Password"
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New Password"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm New Password"
    )
    
    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']