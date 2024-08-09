from django.urls import path
from . import views

urlpatterns = [
	path('', views.atdb, name = 'atdb'),
]