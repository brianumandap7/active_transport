from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from login import views as user_views
from .forms import CustomAuthForm
from . import views


urlpatterns = [
	path('', auth_views.LoginView.as_view(template_name='login/login.html', redirect_authenticated_user = True, authentication_form=CustomAuthForm), name = 'login'),
	path('logout/', views.lout, name = 'login-logout'),
]