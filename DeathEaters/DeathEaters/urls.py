
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/',views.home.as_view(),name = 'homepage'),
    path('loginPage/',views.Login.as_view(),name = 'Login'),
    path('logoutPage/',views.Logout.as_view(),name= 'Logout'),
]
