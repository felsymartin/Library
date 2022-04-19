from django.urls import path
from . import views

urlpatterns = [
    # path('',views.bookdetails, name='bookdetails'),
    path('<int:pageid>/',views.session, name='session'),
    
]