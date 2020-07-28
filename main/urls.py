from django.urls import path

from . import views
from .views import BlogListView,BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('query_send', views.query_send,name="query_send"),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
]