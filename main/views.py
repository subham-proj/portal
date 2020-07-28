from django.shortcuts import render,redirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views import View
from .models import Query,Category
# Create your views here.


def query_send(request):
    email = request.POST["email"]
    query = request.POST["query"]

    add = Query(email=email,query=query)

    add.save()
    # messages.success(request,'Your Query has been submitted successfully!')

    return redirect('/')



def BlogListView(request):
    return render(request,'blog/blog_list.html')