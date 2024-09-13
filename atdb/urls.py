from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import ATDBView, TowTblView, RTView, ATView, RSView, CLView, FSView, MView, towDB, regDB, areDB, roaDB, claDB, funDB, bikDB

urlpatterns = [
    path('', staff_member_required(ATDBView.as_view()), name='atdb'),
    path('towtbl/', staff_member_required(TowTblView.as_view()), name='towtbl'),
    path('rt/', staff_member_required(RTView.as_view()), name='rt'),
    path('at/', staff_member_required(ATView.as_view()), name='at'),
    path('rs/', staff_member_required(RSView.as_view()), name='rs'),
    path('cl/', staff_member_required(CLView.as_view()), name='cl'),
    path('fs/', staff_member_required(FSView.as_view()), name='fs'),
    path('maindb/', staff_member_required(MView.as_view()), name='maindb'),
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
]