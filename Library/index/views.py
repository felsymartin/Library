from django.shortcuts import render
from django.http import HttpResponse
from bookdetails.models import books
# Create your views here.

prolist = books.objects.all()

def index(request):
    return render(request,'index.html',{'Pro':prolist})

def search(request):
    if 'search' in request.GET:
        search = request.GET['search']
        data = books.objects.filter(name=search)
    else:
        data = books.objects.all()
    context = {
            'data' : data
        }
    return render (request,'index.html', context)
