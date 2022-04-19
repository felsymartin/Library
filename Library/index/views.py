from django.shortcuts import render
from django.http import HttpResponse
from bookdetails.models import books
# Create your views here.

prolist = books.objects.all()

def index(request):
    return render(request,'index.html',{'Pro':prolist})
