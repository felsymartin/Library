from django.urls import path
from . import views

urlpatterns = [
    path('registerlogin/',views.registerlogin, name='registerlogin'),
    path('registerlogin/register', views.register, name='register'),
    path('registerlogin/login', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
]