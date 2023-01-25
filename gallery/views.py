from django.shortcuts import render
from .models import Video 
# Create your views here.
def showGallery (request):
    videos = Video.objects.all()
    return render (request,'galleryApp/gallery.html',context={'videos':videos})
