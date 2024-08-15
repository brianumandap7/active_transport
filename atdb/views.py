from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from .models import Typeofwork


# Create your views here.
def atdb(request):
	query = {
		
	}
	return render(request, 'atdb/atdb.html', query)

def towtbl(request):
	query = {
		'tow': Typeofwork.objects.all(),
	}
	return render(request, 'atdb/towtbl.html', query)
