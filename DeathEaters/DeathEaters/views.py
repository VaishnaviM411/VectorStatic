import os
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic.base import View
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from surveyor.models import HouseHolds 
from surveyor.models import HouseListing
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
import shortuuid

class home(View):
    def get(self, request):
        return render(request, 'home.html')

class Login(View):
    def get(self, request, template_name='login.html'):
        return render(request,template_name)

    def post(self, request, template_name='login.html'):
        message = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            message['user']=user
        else:
            message['message']='User not authenticated'        
        return render(request,template_name='household.html')


class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, 'home.html')
        
class surveyorPage(View):
    def get(self, request):
        return render(request, 'surveyorPage.html')

class analystPage(View):
    def get(self, request):
        return render(request, 'analystPage.html')

