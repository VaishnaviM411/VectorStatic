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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        group = None
        if user is not None:
            if user.is_active:
                login(request, user)
                group = user.groups.all()[0].name
                if group == 'surveyor_group':
                    return redirect('surveyor:surveyorPage')
                if group == 'analyst_group':
                    return redirect('analyst:analystPage')
                else:
                    return render(request, 'home.html')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid Login'})



class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, 'home.html')
        


class analystPage(View):
    def get(self, request):
        return render(request, 'analystPage.html')

