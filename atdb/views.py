from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from .models import Typeofwork, Region, BikeArea, RoadSection, BikeClass, FundSource, bikelanetbl, TypeofworkAuditLog, RegionAuditLog, BikeAreaAuditLog, RoadSectionAuditLog, BikeClassAuditLog, FundSourceAuditLog, BikelaneAuditLog
from django.views.generic import TemplateView, ListView
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .forms import TypeofworkForm, RegionForm, BikeAreaForm, RoadSectionForm, BikeClassForm, FundSourceForm, BikelaneForm, ExcelUploadForm, UploadFileForm
from django.contrib import messages
from django.forms.models import model_to_dict
from django.utils import timezone

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

import openpyxl

from django.views import View  # Ensure this is imported

import pandas as pd

from datetime import datetime

from .serializers import BikelaneTblSerializer


#edit type of work
def edit_typeofwork(request, tag):
    # Get the instance to be edited
    typeofwork = get_object_or_404(Typeofwork, Typeofwork_id=tag)
    old_value = typeofwork.Typeofwork

    if request.method == 'POST':
        form = TypeofworkForm(request.POST, instance=typeofwork)
        if form.is_valid():
            new_value = form.cleaned_data['Typeofwork']
            if old_value != new_value:
                form.save()

                TypeofworkAuditLog.objects.create(
                    typeofwork=typeofwork,
                    edited_by=request.user,  # Assuming you have authentication
                    old_value=old_value,
                    new_value=new_value
                )
            messages.success(request, 'Type of Work updated successfully.')
            return redirect('/atdb/towtbl')  # Redirect to a success page
    else:
        form = TypeofworkForm(instance=typeofwork)
        tag = tag

    return render(request, 'atdb/edit_typeofwork.html', {'form': form, 'tag': tag, 'messages': messages})


#edit regions
def edit_regions(request, tag):

    # Get the instance to be edited
    region = get_object_or_404(Region, Region_id=tag)
    old_value = region.Region
    if request.method == 'POST':
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            new_value = form.cleaned_data['Region']
            if old_value != new_value:
                form.save()

                RegionAuditLog.objects.create(
                    Region=region,
                    edited_by=request.user,  # Assuming you have authentication
                    old_value=old_value,
                    new_value=new_value
                )
            messages.success(request, 'Region updated successfully.')
            return redirect('/atdb/rt')  # Redirect to a success page
    else:
        form = RegionForm(instance=region)
        tag = tag
    return render(request, 'atdb/edit_regions.html', {'form': form, 'tag': tag, 'messages': messages})

#edit areas
def edit_areas(request, tag):
    area = get_object_or_404(BikeArea, BikeArea_id = tag)
    old_value = area.BikeArea
    if request.method == 'POST':
        form = BikeAreaForm(request.POST, instance = area)
        if form.is_valid():
            new_value = form.cleaned_data['BikeArea']
            if old_value != new_value:
                form.save()

                BikeAreaAuditLog.objects.create(
                    BikeArea = area,
                    edited_by = request.user,
                    old_value = old_value,
                    new_value = new_value
                )
            messages.success(request, 'Region updated successfully.')
            return redirect('/atdb/at')  # Redirect to a success page
    else:
        form = BikeAreaForm(instance = area)
        tag = tag
    return render(request, 'atdb/edit_areas.html', {'form': form, 'tag': tag, 'messages': messages})

#edit road sections
def edit_roadsections(request, tag):
    road = get_object_or_404(RoadSection, RoadSection_id = tag)
    old_value = road.RoadSection
    if request.method == 'POST':
        form = RoadSectionForm(request.POST, instance = road)
        if form.is_valid():
            new_value = form.cleaned_data['RoadSection']
            if old_value != new_value:
                form.save()

                RoadSectionAuditLog.objects.create(
                    RoadSection = road,
                    edited_by = request.user,
                    old_value = old_value,
                    new_value = new_value
                )
            messages.success(request, 'Road Section updated successfully.')
            return redirect('/atdb/rs')  # Redirect to a success page
    else:
        form = RoadSectionForm(instance = road)
        tag = tag
    return render(request, 'atdb/edit_roadsections.html', {'form': form, 'tag': tag, 'messages': messages})

#edit classes
def edit_classes(request, tag):
    classes = get_object_or_404(BikeClass, BikeClass_id = tag)
    old_value = classes.BikeClass
    if request.method == 'POST':
        form = BikeClassForm(request.POST, instance = classes)
        if form.is_valid():
            new_value = form.cleaned_data['BikeClass']
            if old_value != new_value:
                form.save()

                BikeClassAuditLog.objects.create(
                    BikeClass = classes,
                    edited_by = request.user,
                    old_value = old_value,
                    new_value = new_value
                )
            messages.success(request, 'Class updated successfully.')
            return redirect('/atdb/cl')  # Redirect to a success page
    else:
        form = BikeClassForm(instance = classes)
        tag = tag
    return render(request, 'atdb/edit_classes.html', {'form': form, 'tag': tag, 'messages': messages})

#edit fund sources
def edit_fundsources(request, tag):
    fs = get_object_or_404(FundSource, FundSource_id = tag)
    old_value = fs.FundSource
    if request.method == 'POST':
        form = FundSourceForm(request.POST, instance = fs)
        if form.is_valid():
            new_value = form.cleaned_data['FundSource']
            if old_value != new_value:
                form.save()

                FundSourceAuditLog.objects.create(
                    FundSource = fs,
                    edited_by = request.user,
                    old_value = old_value,
                    new_value = new_value
                )
            messages.success(request, 'Fund Source updated successfully.')
            return redirect('/atdb/fs')  # Redirect to a success page
    else:
        form = FundSourceForm(instance = fs)
        tag = tag
    return render(request, 'atdb/edit_fundsources.html', {'form': form, 'tag': tag, 'messages': messages})

#edit main db
def edit_maintbl(request, tag):
    # Get the specific Bikelane record
    bikelane = get_object_or_404(bikelanetbl, Bikelane_id=tag)

    if request.method == 'POST':
        form = BikelaneForm(request.POST, instance=bikelane)
        if form.is_valid():
            old_data = model_to_dict(bikelane)
            form.save()
            new_data = form.cleaned_data

            BikelaneAuditLog.objects.create(
                bikelane=bikelane,
                changed_by=request.user,
                change_date=timezone.now(),
                action="Updated",
                old_data=str(old_data),
                new_data=str(new_data)
            )

            messages.success(request, 'Main DB updated successfully.')
            return redirect('/atdb/maindb')  # Redirect to a success page after save
    else:
        form = BikelaneForm(instance=bikelane)

    return render(request, 'atdb/edit_maintbl.html', {'form': form, 'bikelane': bikelane, 'messages': messages})

class add_tow(CreateView):
    model = Typeofwork
    form_class = TypeofworkForm
    template_name = 'atdb/add_tow.html'  # The template for the form
    success_url = reverse_lazy('towtbl')

class add_rt(CreateView):
    model = Region
    form_class = RegionForm
    template_name = 'atdb/add_rt.html'  # The template for the form
    success_url = reverse_lazy('rt')

class add_rt(CreateView):
    model = Region
    form_class = RegionForm
    template_name = 'atdb/add_rt.html'  # The template for the form
    success_url = reverse_lazy('rt')

class add_at(CreateView):
    model = BikeArea
    form_class = BikeAreaForm
    template_name = 'atdb/add_at.html'  # The template for the form
    success_url = reverse_lazy('at')

class add_rs(CreateView):
    model = RoadSection
    form_class = RoadSectionForm
    template_name = 'atdb/add_rs.html'  # The template for the form
    success_url = reverse_lazy('rs')

class add_cl(CreateView):
    model = BikeClass
    form_class = BikeClassForm
    template_name = 'atdb/add_cl.html'  # The template for the form
    success_url = reverse_lazy('cl')

class add_fs(CreateView):
    model = FundSource
    form_class = FundSourceForm
    template_name = 'atdb/add_fs.html'  # The template for the form
    success_url = reverse_lazy('fs')

class add_maindb(CreateView):
    model = bikelanetbl
    form_class = BikelaneForm
    template_name = 'atdb/add_maindb.html'  # The template for the form
    success_url = reverse_lazy('maindb')

def del_maindb(request, tag):
    # Get the bikelanetbl instance with the specified Bikelane_id or return 404 if not found
    bikelane = get_object_or_404(bikelanetbl, Bikelane_id=tag)
    
    # Update the status field to 0

    old_data = ""
    new_data = f"Archived {bikelane.Bikelane_Code}"

    bikelane.status = 0
    bikelane.save()


    BikelaneAuditLog.objects.create(
        bikelane=bikelane,
        changed_by=request.user,
        change_date=timezone.now(),
        action="Updated",
        old_data=old_data,
        new_data=new_data
    )
    
    # Optionally, redirect to a success page or return a response
    return redirect('/atdb/maindb')

def un_maindb(request, tag):
    # Get the bikelanetbl instance with the specified Bikelane_id or return 404 if not found
    bikelane = get_object_or_404(bikelanetbl, Bikelane_id=tag)
    
    # Update the status field to 0

    old_data = ""
    new_data = f"Unarchived {bikelane.Bikelane_Code}"

    bikelane.status = 1
    bikelane.save()


    BikelaneAuditLog.objects.create(
        bikelane=bikelane,
        changed_by=request.user,
        change_date=timezone.now(),
        action="Updated",
        old_data=old_data,
        new_data=new_data
    )
    
    # Optionally, redirect to a success page or return a response
    return redirect('/atdb/maindb')

def hist(request, tag):
    que = None

    if tag == "tw":
        que = TypeofworkAuditLog.objects.all()
        tag = "Types of Work Table"
    elif tag == "rt":
        que = RegionAuditLog.objects.all()
        tag = "Region Table"
    elif tag == "at":
        que = BikeAreaAuditLog.objects.all()
        tag = "Area Table"
    elif tag == "rs":
        que = RoadSectionAuditLog.objects.all()
        tag = "Road Section Table"
    elif tag == "cl":
        que = BikeClassAuditLog.objects.all()
        tag = "Class Table"
    elif tag == "fs":
        que = FundSourceAuditLog.objects.all()
        tag = "Fund Source Table"
    elif tag == "maindb":
        que = BikelaneAuditLog.objects.all()
        tag = "Bike Lane Table"

    context = {
        'tag': tag,
        'que': que,
    }
    return render(request, 'atdb/hist.html', context)
# Create your views here.
class ATDBView(TemplateView):
    template_name = 'atdb/atdb.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            # Add any additional context if needed
        })
        return context

class TowTblView(ListView):
    model = Typeofwork
    template_name = 'atdb/towtbl.html'
    context_object_name = 'tow'
    app_label = 'atdb'  # Define the app label here

    def handle_no_permission(self):
        return super().handle_no_permission()

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Use the defined app_label
        model_name = self.model._meta.model_name  # e.g., 'typeofwork'
        permission_string = f'{self.app_label}.change_{model_name}'  # Construct the permission string
        add_permission_string = f'{self.app_label}.add_{model_name}'
        view_permission_string = f'{self.app_label}.view_{model_name}'

        # Check if the user has the constructed permission
        context['has_permission'] = self.request.user.has_perm(permission_string)
        context['can_add'] = self.request.user.has_perm(add_permission_string)
        context['can_view'] = self.request.user.has_perm(view_permission_string)
        context['user_permissions'] = self.request.user.get_all_permissions()
        
        return context

class RTView(ListView):
    model = Region
    template_name = 'atdb/rt.html'
    context_object_name = 'rt'
    app_label = 'atdb'  # Define the app label here

    def handle_no_permission(self):
        return super().handle_no_permission()

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Use the defined app_label
        model_name = self.model._meta.model_name  # e.g., 'region'
        permission_string = f'{self.app_label}.change_{model_name}'  # Construct the permission string
        add_permission_string = f'{self.app_label}.add_{model_name}'
        view_permission_string = f'{self.app_label}.view_{model_name}'

        # Check if the user has the constructed permission
        context['has_permission'] = self.request.user.has_perm(permission_string)
        context['can_add'] = self.request.user.has_perm(add_permission_string)
        context['can_view'] = self.request.user.has_perm(view_permission_string)
        context['user_permissions'] = self.request.user.get_all_permissions()
        
        return context

class ATView(ListView):
    model = BikeArea
    template_name = 'atdb/at.html'
    context_object_name = 'at'
    app_label = 'atdb'

    def handle_no_permission(self):
        return super().handle_no_permission

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Dynamically construct the permission string for 'change' action on the BikeArea model
        model_name = self.model._meta.model_name  # 'bikearea'
        permission_string = f'{self.app_label}.change_{model_name}'  # Construct the permission string
        add_permission_string = f'{self.app_label}.add_{model_name}'
        view_permission_string = f'{self.app_label}.view_{model_name}'

        # Check if the user has the constructed permission
        context['has_permission'] = self.request.user.has_perm(permission_string)
        context['can_add'] = self.request.user.has_perm(add_permission_string)
        context['can_view'] = self.request.user.has_perm(view_permission_string)
        context['user_permissions'] = self.request.user.get_all_permissions()
        
        return context

class RSView(ListView):
    model = RoadSection
    template_name = 'atdb/rs.html'
    context_object_name = 'rs'
    app_label = 'atdb'  # Define the app label here

    def handle_no_permission(self):
        return super().handle_no_permission()

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Use the defined app_label
        model_name = self.model._meta.model_name  # e.g., 'roadsection'
        permission_string = f'{self.app_label}.change_{model_name}'  # Construct the permission string
        add_permission_string = f'{self.app_label}.add_{model_name}'
        view_permission_string = f'{self.app_label}.view_{model_name}'

        # Check if the user has the constructed permission
        context['has_permission'] = self.request.user.has_perm(permission_string)
        context['can_add'] = self.request.user.has_perm(add_permission_string)
        context['can_view'] = self.request.user.has_perm(view_permission_string)
        context['user_permissions'] = self.request.user.get_all_permissions()
        
        return context

class CLView(ListView):
    model = BikeClass
    template_name = 'atdb/cl.html'
    context_object_name = 'cl'
    app_label = 'atdb'  # Define the app label here

    def handle_no_permission(self):
        return super().handle_no_permission()

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Use the defined app_label
        model_name = self.model._meta.model_name  # e.g., 'bikeclass'
        permission_string = f'{self.app_label}.change_{model_name}'  # Construct the permission string
        add_permission_string = f'{self.app_label}.add_{model_name}'
        view_permission_string = f'{self.app_label}.view_{model_name}'

        # Check if the user has the constructed permission
        context['has_permission'] = self.request.user.has_perm(permission_string)
        context['can_add'] = self.request.user.has_perm(add_permission_string)
        context['can_view'] = self.request.user.has_perm(view_permission_string)
        context['user_permissions'] = self.request.user.get_all_permissions()
        
        return context

class FSView(ListView):
    model = FundSource
    template_name = 'atdb/fs.html'
    context_object_name = 'fs'
    app_label = 'atdb'  # Define the app label here

    def handle_no_permission(self):
        return super().handle_no_permission()

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Use the defined app_label
        model_name = self.model._meta.model_name  # e.g., 'fundsource'
        permission_string = f'{self.app_label}.change_{model_name}'  # Construct the permission string
        add_permission_string = f'{self.app_label}.add_{model_name}'
        view_permission_string = f'{self.app_label}.view_{model_name}'

        # Check if the user has the constructed permission
        context['has_permission'] = self.request.user.has_perm(permission_string)
        context['can_add'] = self.request.user.has_perm(add_permission_string)
        context['can_view'] = self.request.user.has_perm(view_permission_string)
        context['user_permissions'] = self.request.user.get_all_permissions()
        
        return context

class MView(ListView):
    model = bikelanetbl
    template_name = 'atdb/maindb.html'
    context_object_name = 'maindb'
    app_label = 'atdb'  # Define the app label here

    def handle_no_permission(self):
        return super().handle_no_permission()

    def get_queryset(self):
        return super().get_queryset().filter(status=1).order_by('Bikelane_id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Use the defined app_label
        model_name = self.model._meta.model_name  # e.g., 'bikelanetbl'
        permission_string = f'{self.app_label}.change_{model_name}'  # Construct the permission string
        add_permission_string = f'{self.app_label}.add_{model_name}'
        view_permission_string = f'{self.app_label}.view_{model_name}'

        # Check if the user has the constructed permission
        context['has_permission'] = self.request.user.has_perm(permission_string)
        context['can_add'] = self.request.user.has_perm(add_permission_string)
        context['can_view'] = self.request.user.has_perm(view_permission_string)
        context['user_permissions'] = self.request.user.get_all_permissions()
        
        return context

class MView_archived(ListView):
    model = bikelanetbl
    template_name = 'atdb/archived.html'
    context_object_name = 'maindb'
    app_label = 'atdb'  # Define the app label here

    def handle_no_permission(self):
        return super().handle_no_permission()

    def get_queryset(self):
        return super().get_queryset().filter(status=0).order_by('Bikelane_id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Use the defined app_label
        model_name = self.model._meta.model_name  # e.g., 'bikelanetbl'
        permission_string = f'{self.app_label}.change_{model_name}'  # Construct the permission string
        add_permission_string = f'{self.app_label}.add_{model_name}'
        view_permission_string = f'{self.app_label}.view_{model_name}'

        # Check if the user has the constructed permission
        context['has_permission'] = self.request.user.has_perm(permission_string)
        context['can_add'] = self.request.user.has_perm(add_permission_string)
        context['can_view'] = self.request.user.has_perm(view_permission_string)
        context['user_permissions'] = self.request.user.get_all_permissions()
        
        return context

class BikelaneBulkUpload(View):
    def get(self, request):
        form = ExcelUploadForm()
        return render(request, 'atdb/bikelane_bulk_upload.html', {'form': form})

    def post(self, request):
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']

            # Read the Excel file with custom column names
            df = pd.read_excel(excel_file, sheet_name=6, header=None, skiprows=1)
            df.columns = [
                "Bikelane_Code", "Typeofwork_ID", "Region_ID", "BikeArea_ID",
                "RoadSection_ID", "Length", "StartPointX", "StartPointY",
                "EndPointX", "EndPointY", "BikeClass_ID", "BikeDate",
                "FundSource_ID", "Remarks", "Province"
            ]

            df['Remarks'].fillna('No remarks', inplace=True)
            df['Remarks'].replace('', 'No remarks', inplace=True)

            # Iterate over the rows in the DataFrame
            for _, row in df.iterrows():
                # Handle BikeDate: Convert to string in ISO format or set to None if invalid
                bike_date = row['BikeDate']
                if pd.notnull(bike_date) and isinstance(bike_date, datetime):
                    # Convert valid datetime to string format
                    bike_date = bike_date.strftime('%Y-%m-%d')
                else:
                    # Set invalid or missing dates to None
                    bike_date = None
                

                # Create a new bikelanetbl instance
                bikelane_instance = bikelanetbl(
                    Bikelane_Code=row['Bikelane_Code'],
                    Typeofwork_id=row['Typeofwork_ID'],
                    Region_id=row['Region_ID'],
                    BikeArea_id=row['BikeArea_ID'],
                    RoadSection_id=row['RoadSection_ID'],
                    Length=row['Length'],
                    StartPointX=row['StartPointX'],
                    StartPointY=row['StartPointY'],
                    EndPointX=row['EndPointX'],
                    EndPointY=row['EndPointY'],
                    BikeClass_id=row['BikeClass_ID'],
                    BikeDate=bike_date,  # Only valid dates or None
                    FundSource_id=row['FundSource_ID'],
                    Remarks=row['Remarks'],
                    Province=row['Province']
                )
                bikelane_instance.save()

            return redirect('/atdb/maindb')

        return JsonResponse({"error": "Invalid form"}, status=400)

class RoadSectionBulkUpload(View):
    def get(self, request):
        form = ExcelUploadForm()  # Create an instance of your form
        return render(request, 'atdb/roadsection_bulk_upload.html', {'form': form})  # Adjust template name as needed

    def post(self, request):
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():  # Check if the form is valid
            excel_file = request.FILES['file']  # Get the uploaded file

            # Read the Excel file, specifying the second sheet (index 1)
            df = pd.read_excel(excel_file, sheet_name=1, header=None, skiprows=1)

            # Iterate over the rows in the DataFrame
            for _, row in df.iterrows():
                # Use the column index to access data
                road_section_instance = RoadSection(
                    RoadSection=row[0]  # Adjust the index if the column order changes
                )
                # Save the instance to the database
                road_section_instance.save()

            return redirect('/atdb/rs')

        return JsonResponse({"error": "Invalid form"}, status=400)

class BikeAreaBulkUpload(View):
    def get(self, request):
        form = ExcelUploadForm()  # Create an instance of your form
        return render(request, 'atdb/bikearea_bulk_upload.html', {'form': form})  # Adjust template name as needed

    def post(self, request):
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():  # Check if the form is valid
            excel_file = request.FILES['file']  # Get the uploaded file

            # Read the Excel file, specifying the third sheet (index 2)
            df = pd.read_excel(excel_file, sheet_name=2, header=None, skiprows=1)

            # Print the DataFrame to debug
            print(df)

            # Iterate over the rows in the DataFrame
            for _, row in df.iterrows():
                bike_area_name = row[0]  # Assuming the first column has the bike area name
                if pd.notna(bike_area_name):  # Check if the value is not NaN
                    bike_area_instance = BikeArea(
                        BikeArea=bike_area_name
                    )
                    bike_area_instance.save()
                    print(f"Saved BikeArea: {bike_area_instance.BikeArea}")
                else:
                    print(f"Skipped row with NaN value: {row}")

            return redirect('/atdb/at')

        return JsonResponse({"error": "Invalid form"}, status=400)

class RegionBulkUpload(View):
    def get(self, request):
        form = ExcelUploadForm()  # Create an instance of your form
        return render(request, 'atdb/region_bulk_upload.html', {'form': form})  # Adjust template name as needed

    def post(self, request):
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():  # Check if the form is valid
            excel_file = request.FILES['file']  # Get the uploaded file

            # Read the Excel file, specifying the third sheet (index 2)
            df = pd.read_excel(excel_file, sheet_name=5, header=None, skiprows=1)

            # Print the DataFrame to debug
            print(df)

            # Iterate over the rows in the DataFrame
            for _, row in df.iterrows():
                region = row[0]  # Assuming the first column has the bike area name
                if pd.notna(region):  # Check if the value is not NaN
                    region = Region(
                        Region=region
                    )
                    region.save()
                    print(f"Saved Region: {region.Region}")
                else:
                    print(f"Skipped row with NaN value: {row}")

            return redirect('/atdb/rt')

        return JsonResponse({"error": "Invalid form"}, status=400)

class towDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(Typeofwork.objects.values())
        return Response(prog)

class regDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(Region.objects.values())
        return Response(prog)

class areDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(BikeArea.objects.values())
        return Response(prog)

class roaDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(RoadSection.objects.values())
        return Response(prog)

class claDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(BikeClass.objects.values())
        return Response(prog)

class funDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        prog = list(FundSource.objects.values())
        return Response(prog)

class bikDB(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        prog = bikelanetbl.objects.filter(status = 1)
        serializer = BikelaneTblSerializer(prog, many=True)
        return Response(serializer.data)

