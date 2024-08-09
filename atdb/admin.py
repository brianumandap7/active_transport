from django.contrib import admin
from .models import bikelanetbl, Typeofwork, Region, BikeArea, RoadSection, BikeClass, FundSource
from import_export.admin import ImportExportModelAdmin, ExportActionMixin

class exportSurvey(ExportActionMixin, admin.ModelAdmin):
	pass
# Register your models here.

admin.site.register(bikelanetbl, exportSurvey)
admin.site.register(Typeofwork, exportSurvey)
admin.site.register(Region, exportSurvey)
admin.site.register(BikeArea, exportSurvey)
admin.site.register(RoadSection, exportSurvey)
admin.site.register(BikeClass, exportSurvey)
admin.site.register(FundSource, exportSurvey)