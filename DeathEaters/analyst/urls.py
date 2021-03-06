
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'analyst'

urlpatterns = [
    path('analystPage/', views.analystPage.as_view(),name = 'analystPage'),
    path('houseListQueries', views.houseListQueries.as_view(),name = 'houseListQueries'),
    path('houseHoldQueries', views.houseHoldQueries.as_view(),name = 'houseHoldQueries'),
    path('houseListQueryResult', views.houseListQueryResult.as_view(),name = 'houseListQueryResult'),
    path('houseHoldQueryResult', views.houseHoldQueryResult.as_view(),name = 'houseHoldQueryResult'),
]
