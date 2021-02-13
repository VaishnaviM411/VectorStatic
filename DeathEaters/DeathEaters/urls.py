
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home.as_view(),name = 'homepage'),
    path('loginPage/',views.Login.as_view(),name = 'Login'),
    path('logoutPage/',views.Logout.as_view(),name= 'Logout'),
    path('surveyorPage', views.surveyorPage.as_view(),name = 'surveyorPage'),
    path('analystPage', views.analystPage.as_view(),name = 'analystPage'),
]
