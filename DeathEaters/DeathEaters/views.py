import os
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic.base import View
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from DeathEaters.models import HouseHolds 
from DeathEaters.models import HouseListing
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
import shortuuid

class home(View):
    

class login(View):
     
class houselisting(View):
    
class households(View):
     