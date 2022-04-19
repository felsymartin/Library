from django.shortcuts import render
from .models import books

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
        previous = [1]
        request.session['recent_view'] = [pageid]
    request.session.modified = True
    print("Show Id",request.session['recent_view'])

    return render(request,'bdetails.html',{'bookid':obj_id,'prev':previous})
