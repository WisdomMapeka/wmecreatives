from django.shortcuts import render, get_object_or_404
from . models import Blog, Tags, HomePage,Author, YoutubeVideos



# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def bloglist(request):
    return render(request, 'blog/bloglist.html')

def blogdetail(request):
    return render(request, 'blog/blogdetail.html')
