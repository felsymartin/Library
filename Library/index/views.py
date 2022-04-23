from django.shortcuts import render,redirect
from django.http import HttpResponse
from bookdetails.models import books
from django.conf import settings
from django.core.mail import send_mail
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

def email(request):
    name = request.POST['Name']
    mail = request.POST['Email']
    phone = request.POST['Phone']
    msg = request.POST['message']
    support_email = ['felsydjango@gmail.com']
    subject = 'Customer support from Book Worm'
    mailmsg = f'''Hi Felsy. I like to inform that Mr/Ms {name} given a contact message.
    The message was {msg}

    email: {mail}
    phone no: {phone}
    ''' 
    email_form = settings.EMAIL_HOST_USER
    send_mail(subject,mailmsg,email_form,support_email)

    return redirect('/')