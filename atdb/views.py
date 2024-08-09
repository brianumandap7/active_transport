from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse


# Create your views here.
def atdb(request):
	query = {
		
	}
	return render(request, 'atdb/atdb.html', query)
