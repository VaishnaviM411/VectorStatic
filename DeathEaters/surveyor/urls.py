
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('houseListing/',views.houselisting.as_view(),name ='houselisting'),
    path('houseHolds/',views.households.as_view(),name='households'),
]
