
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/',views.home.as_view(),name = 'homepage'),
    path('loginPage/',views.login.as_view(),name = 'loginpage'),
    path('houseListing/',views.houselisting.as_view(),name ='houselisting'),
    path('houseHolds/',views.households.as_view(),name='households'),
]
