from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import ATDBView, TowTblView, RTView, ATView, RSView, CLView, FSView, MView

urlpatterns = [
    path('', staff_member_required(ATDBView.as_view()), name='atdb'),
    path('towtbl/', staff_member_required(TowTblView.as_view()), name='towtbl'),
    path('rt/', staff_member_required(RTView.as_view()), name='rt'),
    path('at/', staff_member_required(ATView.as_view()), name='at'),
    path('rs/', staff_member_required(RSView.as_view()), name='rs'),
    path('cl/', staff_member_required(CLView.as_view()), name='cl'),
    path('fs/', staff_member_required(FSView.as_view()), name='fs'),
    path('maindb/', staff_member_required(MView.as_view()), name='maindb'),
]