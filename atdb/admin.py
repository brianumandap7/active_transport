from django.contrib import admin
from .models import bikelanetbl, Typeofwork, Region, BikeArea, RoadSection, BikeClass, FundSource, TypeofworkAuditLog, RegionAuditLog, BikeAreaAuditLog, RoadSectionAuditLog, BikeClassAuditLog, FundSourceAuditLog, BikelaneAuditLog
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
admin.site.register(TypeofworkAuditLog, exportSurvey)
admin.site.register(RegionAuditLog, exportSurvey)
admin.site.register(BikeAreaAuditLog, exportSurvey)
admin.site.register(RoadSectionAuditLog, exportSurvey)
admin.site.register(BikeClassAuditLog, exportSurvey)
admin.site.register(FundSourceAuditLog, exportSurvey)
admin.site.register(BikelaneAuditLog, exportSurvey)