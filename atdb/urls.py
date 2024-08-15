from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('', login_required(views.atdb), name = 'atdb'),
	path('towtbl/', login_required(views.towtbl), name = 'towtbl'),
]