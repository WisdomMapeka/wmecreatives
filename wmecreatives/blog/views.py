from django.shortcuts import render, get_object_or_404
from . models import Blog, Tags, HomePage,Author, YoutubeVideos, TodaysCode, Categories
import datetime



# Create your views here.
def index(request):
    today = datetime.date.today()
    home_record = HomePage.objects.all().first()
    todayscode = TodaysCode.objects.filter(date_created__gt = today).first()
    blogs = Blog.objects.all()[:4]
    categories = Categories.objects.all()
    return render(request, 'blog/index.html', {'home_record':home_record,
                                               'todayscode':todayscode,
                                               'blogs':blogs,
                                               'categories':categories})

def bloglist(request):
    return render(request, 'blog/bloglist.html')

def blogdetail(request):
    return render(request, 'blog/blogdetail.html')
