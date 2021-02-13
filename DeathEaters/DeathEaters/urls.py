
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home.as_view(),name = 'home'),
    path('loginPage/',views.Login.as_view(),name = 'Login'),
    path('logoutPage/',views.Logout.as_view(),name= 'Logout'),
    path('surveyor/', include('surveyor.urls', namespace='surveyor')),
    path('analyst/', include('analyst.urls', namespace='analyst')),
]
