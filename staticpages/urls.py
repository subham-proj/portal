from django.urls import path
from . import views

urlpatterns = [
        path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact'),
        path('privacy/', views.privacy, name='privacy'),
        path('contribute/', views.contribute, name='contribute'),
        path('contact/lead', views.lead,name="lead"),


]