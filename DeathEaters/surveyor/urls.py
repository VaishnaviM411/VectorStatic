
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'surveyor'

urlpatterns = [
    path('surveyorPage', views.surveyorPage.as_view(),name = 'surveyorPage'),
    path('houselisting/',views.houselisting.as_view(),name ='houselisting'),
    path('households/',views.households.as_view(),name='households'),
    
]
