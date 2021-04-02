from django.shortcuts import render, get_object_or_404
from . models import Blog, Tags, HomePage,Author, YoutubeVideos
from random import randint
import random

# Create your views here.
def index(request):
    all_articles = Blog.objects.all()
    homepage = HomePage.objects.all().first()
    recent_articles = Blog.objects.all().order_by('date')[:4]
    youtube_links = YoutubeVideos.objects.all()[:4]

    q = YoutubeVideos.objects.all()
    item_count = q.count()
    if item_count:
        random_link = q[random.randint(0,item_count+1)]
    else:
        random_link=None

    return render(request, 'blog/index.html', {'all_articles':all_articles, 
                                               'homepage':homepage,
                                               'recent_articles':recent_articles,
                                               'random_link':random_link,
                                               'youtube_links':youtube_links})





def article_details(request, slug):
  article = get_object_or_404(Blog, slug=slug)
  youtube_links = YoutubeVideos.objects.all()[:4]
  related_articles = Blog.objects.filter(tag=article.tag.first())
  return render(request, 'blog/aticle-details.html', {'article':article,
                                                      'youtube_links':youtube_links,
                                                      'related_articles':related_articles})


def article_list(request, tag):
  if Tags.objects.filter(tag=tag).first()=='NoneType':
    tags = 0
  else:
    tags = Tags.objects.filter(tag=tag).first()
  article_list = Blog.objects.filter(tag=tags)
  youtube_links = YoutubeVideos.objects.all()[:4]
  return render(request, 'blog/main-menu-article-list.html', {'articles':article_list,
                                                      'youtube_links':youtube_links})
