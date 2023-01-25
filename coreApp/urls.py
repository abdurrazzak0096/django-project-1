from django.urls import path 
from coreApp import views 

urlpatterns = [
    path('contact/',views.contact,name='contact'),
]