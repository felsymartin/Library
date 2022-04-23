from django.shortcuts import render,redirect
from .models import books,comment

# Create your views here.

prolist = books.objects.all()

def bookdetails(request):
    book_id = request.GET['id']
    obj_id = books.objects.get(id = book_id)
    return render(request,'bdetails.html',{'bookid':obj_id})
    

def session(request,pageid):
    
    obj_id = books.objects.get(id=pageid)
    if 'recent_view' in request.session:                
        if pageid in request.session['recent_view']:

            request.session['recent_view'].remove (pageid)
        previous = books.objects.filter(id__in= request.session['recent_view'])
        print("Previous view:",previous)
        request.session['recent_view'].insert(0,pageid)
        # To limit the length of product in list
        if len(request.session['recent_view'])>4:
            request.session['recent_view'].pop()

    else:
        previous = [pageid]
        request.session['recent_view'] = [pageid]
    request.session.modified = True
    print("Show Id",request.session['recent_view'])

    return render(request,'bdetails.html',{'bookid':obj_id,'prev':previous})

def commenttext(request):
    text = request.GET['txt']
    pro_id = request.GET['bookid']
    username = request.GET['username']
    obj_id = books.objects.get(id=pro_id)

    cmt = comment.objects.create (name = username, book = obj_id, body = text)
    cmt.save();

    #return render(request,'bdetails.html',{'bookid':obj_id})
    return redirect('/details/'+pro_id)