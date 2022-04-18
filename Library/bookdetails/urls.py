from django.urls import path
from . import views

urlpatterns = [
    path('bookdetails',views.bookdetails, name='bookdetails'),
    
]