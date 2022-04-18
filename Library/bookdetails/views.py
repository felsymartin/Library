from django.shortcuts import render

# Create your views here.

def bookdetails(request):
    return render(request,'bdetails.html')
