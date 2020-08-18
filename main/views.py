from django.shortcuts import render,redirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views import View
from .models import Query,Category,Blogs
# Create your views here.


def query_send(request):
    email = request.POST["email"]
    query = request.POST["query"]

    add = Query(email=email,query=query)

    add.save()
    # messages.success(request,'Your Query has been submitted successfully!')

    return redirect('/')



class BlogListView(ListView):

    model = Blogs
    paginate_by = 10  # if pagination is desired
    c1= None
    c2= None
    

    def get_data(self):
        new_context = Blogs.objects.all()
        category = self.request.GET.get('category')
        sub_catgeory = self.request.GET.get('tag')
        if category:
            check = Category.objects.filter(slug=category).first()
            if check:
                self.c1 = check
                new_context = new_context.filter(category=check)

        return new_context

    def get_queryset(self):
        return self.get_data().order_by("-published_on")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = int(self.get_data().count()/10) + 1
        page = 1
        if self.request.GET.get("page"):
            pages = int(self.request.GET.get("page"))
            if 0 < pages <= context['total']:
                page = pages
        context['page'] = page
        context['prev'] = None
        context['next'] = None
        if page > 1:
            context['prev'] = "/?page="+str(page - 1)
        if page != context['total']:
            context['next'] = "/?page="+str(page + 1)
        context['total'] = range(1,context['total']+1)

        context['tag'] = None

        temp_text = ""

        if self.c2:
            context['tag'] = self.c2.content
            temp_text += self.c2.content + " |"

       
        context['recent'] = Blogs.objects.all().order_by("-published_on")[:5]
        return context


class BlogDetailView(DetailView):
    
    model = Blogs
    
    def get_queryset(self):
        new_context = Blogs.objects.filter(slug=self.kwargs['slug'])
        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context['object']

        context['tags'] = Category.objects.all()
        context['blogs'] = Blogs.objects.all()
      

        return context