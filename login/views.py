from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def login(request):
	query = {
		
	}
	return render(request, 'login/login.html', query)