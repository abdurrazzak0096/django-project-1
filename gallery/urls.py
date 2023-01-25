from django.urls import path 
from gallery import views 

urlpatterns = [
    path('show/',views.showGallery,name='show'),
]