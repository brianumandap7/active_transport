from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout


# Create your views here.
def login(request):
	query = {
		
	}
	return render(request, 'login/login.html', query)


def lout(request):
	query = {
		
	}

	logout(request)
	return render(request, 'login/logout.html', query)