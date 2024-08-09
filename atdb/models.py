from time import strptime
from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

class Typeofwork(models.Model):
	Typeofwork_id = models.AutoField(primary_key=True)
	Typeofwork = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.Typeofwork

class Region(models.Model):
	Region_id = models.AutoField(primary_key=True)
	Region = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.Region

class BikeArea(models.Model):
	BikeArea_id = models.AutoField(primary_key=True)
	BikeArea = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.BikeArea

class RoadSection(models.Model):
	RoadSection_id = models.AutoField(primary_key=True)
	RoadSection = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.RoadSection

class BikeClass(models.Model):
	BikeClass_id = models.AutoField(primary_key=True)
	BikeClass = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.BikeClass

class FundSource(models.Model):
	FundSource_id = models.AutoField(primary_key=True)
	FundSource = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.FundSource

class bikelanetbl(models.Model):
    Bikelane_id = models.AutoField(primary_key=True)
    Bikelane_Code = models.CharField(max_length=250, blank=True, null=True)

    Typeofwork = models.ForeignKey(Typeofwork, on_delete=models.CASCADE, null=True, blank=True, related_name="Typeofwork_name")
    Region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, related_name="Region_name")
    BikeArea = models.ForeignKey(BikeArea, on_delete=models.CASCADE, null=True, blank=True, related_name="BikeArea_name")
    RoadSection = models.ForeignKey(RoadSection, on_delete=models.CASCADE, null=True, blank=True, related_name="RoadSection_name")
    Length = models.DecimalField(max_digits=20, decimal_places=10)
    StartPointX = models.DecimalField(max_digits=20, decimal_places=10)
    StartPointY = models.DecimalField(max_digits=20, decimal_places=10)
    EndPointX = models.DecimalField(max_digits=20, decimal_places=10)
    EndPointY = models.DecimalField(max_digits=20, decimal_places=10)
    BikeClass = models.ForeignKey(BikeClass, on_delete=models.CASCADE, null=True, blank=True, related_name="BikeClass_name")
    BikeDate = models.DateField()
    FundSource = models.ForeignKey(FundSource, on_delete=models.CASCADE, null=True, blank=True, related_name="FundSource_name")
    Remarks = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.Bikelane_id)+" "+str(self.Bikelane_Code)

