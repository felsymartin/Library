from django.shortcuts import render
from .models import books

# Create your views here.

prolist = books.objects.all()

def bookdetails(request):
    return render(request,'bdetails.html')
