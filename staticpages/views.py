from django.shortcuts import render,redirect
from main.models import Contact 
from django.contrib import messages

# Create your views here.

def about(request):
    return render(request, 'staticpages/about.html')


def contact(request):
    return render(request, 'staticpages/contact.html')


def privacy(request):
    return render(request, 'staticpages/privacy.html')

def contribute(request):
    return render(request, 'staticpages/contribute.html')

def lead(request):

    fname = request.POST["fname"]
    lname = request.POST["lname"]
    phone = request.POST["phone"]
    email = request.POST["email"]
    sub = request.POST["sub"]
    msg = request.POST.get('msg', False)


    add = Contact(fname=fname,lname=lname,phone=phone,email=email,sub=sub,msg=msg)

    add.save()
    messages.success(request,'Your Query has been submitted successfully!')

    return redirect('/details/contact/')