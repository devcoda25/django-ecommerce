
from django.urls import path
from . import views


urlpatterns = [

    
    path('', views.home, name='home'),
     path('contact/', views.contact_us, name='contact_page'),
     path('contact/', views.blogpage, name='blog'),
   
]