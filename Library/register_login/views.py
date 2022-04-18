from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

# Create your views here.

def registerlogin(request):
    return render(request,'loginregister.html')


def register(request):
    if request.method == 'POST':
      
        uname = request.POST['userid']
        email = request.POST['emailid']
        npsw = request.POST['npsw']
        rpsw = request.POST['rpsw']

        if npsw==rpsw:
            if User.objects.filter(username=uname).exists():
                umsg="The username already exists!!!"
                return render(request,'loginregister.html',{'umsg':umsg})
            elif User.objects.filter(email=email).exists():
                emsg="Email-Id already taken"
                return render(request,'loginregister.html',{'emsg':emsg})
            else:
                user= User.objects.create_user(username=uname,password=npsw,email=email)
                user.save();
                return redirect('/')
        else:
            pmsg="Password doesn't match!!!"
            return render(request,'loginregister.html',{'pmsg':pmsg})

def login(request):
    if request.method == 'GET':
        userid = request.GET['userid']
        psw = request.GET['psw']

        user = auth.authenticate(username=userid,password=psw)
        if user is not None:
            #Login action
            auth.login(request,user)
            return redirect('/')
        else:
            lmsg='Invalid username or password!!!'
            return render(request,'loginregister.html',{'lmsg':lmsg})

def logout(request):
    auth.logout(request)
    return redirect('/')
