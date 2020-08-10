from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'staticpages/about.html')


def contact(request):
    return render(request, 'staticpages/contact.html')


def privacy(request):
    return render(request, 'staticpages/privacy.html')

def contribute(request):
    return render(request, 'staticpages/contribute.html')

