from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, 'staticpages/contact.html')


def privacy(request):
    return render(request, 'staticpages/privacy.html')

