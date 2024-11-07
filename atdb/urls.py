from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import ATDBView, TowTblView, RTView, ATView, RSView, CLView, FSView, MView, towDB, regDB, areDB, roaDB, claDB, funDB, bikDB, add_tow, add_rt, add_at, add_rs, add_cl, add_fs, add_maindb, BikelaneBulkUpload, RoadSectionBulkUpload, BikeAreaBulkUpload, RegionBulkUpload, MView_archived, ClassBulkUpload, FundBulkUpload

urlpatterns = [
    path('', staff_member_required(ATDBView.as_view()), name='atdb'),
    path('towtbl/', staff_member_required(TowTblView.as_view()), name='towtbl'),
    path('rt/', staff_member_required(RTView.as_view()), name='rt'),
    path('at/', staff_member_required(ATView.as_view()), name='at'),
    path('rs/', staff_member_required(RSView.as_view()), name='rs'),
    path('cl/', staff_member_required(CLView.as_view()), name='cl'),
    path('fs/', staff_member_required(FSView.as_view()), name='fs'),
    path('maindb/', staff_member_required(MView.as_view()), name='maindb'),
    path('maindb_archived/', staff_member_required(MView_archived.as_view()), name='maindb_archived'),
    path('towDB/', views.towDB.as_view(), name='towDB'),
    path('regDB/', views.regDB.as_view(), name='regDB'),
    path('areDB/', views.areDB.as_view(), name='areDB'),
    path('roaDB/', views.roaDB.as_view(), name='roaDB'),
    path('claDB/', views.claDB.as_view(), name='claDB'),
    path('funDB/', views.funDB.as_view(), name='funDB'),
    path('bikDB/', views.bikDB.as_view(), name='bikDB'),
    path('edit_typeofwork/<int:tag>/', views.edit_typeofwork, name='edit_typeofwork'),
    path('edit_regions/<int:tag>/', views.edit_regions, name='edit_regions'),
    path('edit_areas/<int:tag>/', views.edit_areas, name='edit_areas'),
    path('edit_roadsections/<int:tag>/', views.edit_roadsections, name='edit_roadsections'),
    path('edit_classes/<int:tag>/', views.edit_classes, name='edit_classes'),
    path('edit_fundsources/<int:tag>/', views.edit_fundsources, name='edit_fundsources'),
    path('edit_maintbl/<int:tag>/', views.edit_maintbl, name='edit_maintbl'),
    path('hist/<str:tag>/', views.hist, name='hist'),
    path('add_tow/',  add_tow.as_view(), name='add_tow'),
    path('add_rt/',  add_rt.as_view(), name='add_rt'),
    path('add_at/',  add_at.as_view(), name='add_at'),
    path('add_rs/',  add_rs.as_view(), name='add_rs'),
    path('add_cl/',  add_cl.as_view(), name='add_cl'),
    path('add_fs/',  add_fs.as_view(), name='add_fs'),
    path('add_maindb/',  add_maindb.as_view(), name='add_maindb'),
    path('add_bulk/', BikelaneBulkUpload.as_view(), name='BikelaneBulkUpload'),
    path('roadsection-bulk-upload/', RoadSectionBulkUpload.as_view(), name='roadsection_bulk_upload'),
    path('area-bulk-upload/', BikeAreaBulkUpload.as_view(), name='area-bulk-upload'),
    path('region-bulk-upload/', RegionBulkUpload.as_view(), name='region-bulk-upload'),
    path('class-bulk-upload/', ClassBulkUpload.as_view(), name='class-bulk-upload'),
    path('fund-bulk-upload/', FundBulkUpload.as_view(), name='fund-bulk-upload'),
    path('del_maindb/<int:tag>/',  views.del_maindb, name='del_maindb'),
    path('un_maindb/<int:tag>/',  views.un_maindb, name='un_maindb'),

    path('upass/', views.update_password, name='upass'),
]

