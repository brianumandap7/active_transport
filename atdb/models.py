from time import strptime
from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils import timezone

class Typeofwork(models.Model):
	Typeofwork_id = models.AutoField(primary_key=True)
	Typeofwork = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.Typeofwork

class TypeofworkAuditLog(models.Model):
    typeofwork = models.ForeignKey(Typeofwork, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Edit by {self.edited_by} on {self.timestamp}"

class Region(models.Model):
	Region_id = models.AutoField(primary_key=True)
	Region = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.Region

class RegionAuditLog(models.Model):
    Region = models.ForeignKey(Region, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Edit by {self.edited_by} on {self.timestamp}"

class BikeArea(models.Model):
	BikeArea_id = models.AutoField(primary_key=True)
	BikeArea = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.BikeArea

class BikeAreaAuditLog(models.Model):
    BikeArea = models.ForeignKey(BikeArea, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Edit by {self.edited_by} on {self.timestamp}"

class RoadSection(models.Model):
	RoadSection_id = models.AutoField(primary_key=True)
	RoadSection = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.RoadSection

class RoadSectionAuditLog(models.Model):
    RoadSection = models.ForeignKey(RoadSection, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Edit by {self.edited_by} on {self.timestamp}"

class BikeClass(models.Model):
	BikeClass_id = models.AutoField(primary_key=True)
	BikeClass = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.BikeClass

class BikeClassAuditLog(models.Model):
    BikeClass = models.ForeignKey(BikeClass, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Edit by {self.edited_by} on {self.timestamp}"

class FundSource(models.Model):
	FundSource_id = models.AutoField(primary_key=True)
	FundSource = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.FundSource

class FundSourceAuditLog(models.Model):
    FundSource = models.ForeignKey(FundSource, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Edit by {self.edited_by} on {self.timestamp}"

class bikelanetbl(models.Model):
    Bikelane_id = models.AutoField(primary_key=True)
    Bikelane_Code = models.CharField(max_length=250, blank=True, null=True)

    Typeofwork = models.ForeignKey(Typeofwork, on_delete=models.CASCADE, null=True, blank=True, related_name="Typeofwork_name")
    Region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, related_name="Region_name")
    BikeArea = models.ForeignKey(BikeArea, on_delete=models.CASCADE, null=True, blank=True, related_name="BikeArea_name")
    RoadSection = models.ForeignKey(RoadSection, on_delete=models.CASCADE, null=True, blank=True, related_name="RoadSection_name")
    Length = models.CharField(max_length=250, blank=True, null=True)
    StartPointX = models.CharField(max_length=250, blank=True, null=True)
    StartPointY = models.CharField(max_length=250, blank=True, null=True)
    EndPointX = models.CharField(max_length=250, blank=True, null=True)
    EndPointY = models.CharField(max_length=250, blank=True, null=True)
    BikeClass = models.ForeignKey(BikeClass, on_delete=models.CASCADE, null=True, blank=True, related_name="BikeClass_name")
    BikeDate = models.DateField(null = True, blank = True)
    FundSource = models.ForeignKey(FundSource, on_delete=models.CASCADE, null=True, blank=True, related_name="FundSource_name")
    Remarks = models.CharField(max_length=250, blank=True, null=True)
    Province = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.Bikelane_id)+" "+str(self.Bikelane_Code)

class BikelaneAuditLog(models.Model):
    bikelane = models.ForeignKey(bikelanetbl, on_delete=models.CASCADE)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    change_date = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=50)  # e.g., "Updated", "Deleted", "Created"
    old_data = models.TextField(blank=True, null=True)  # Store the old values
    new_data = models.TextField(blank=True, null=True)  # Store the new values

    def __str__(self):
        return f"{self.bikelane.Bikelane_Code} {self.action} by {self.changed_by} on {self.change_date}"

