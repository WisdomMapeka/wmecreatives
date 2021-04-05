from django.shortcuts import render, get_object_or_404
from . models import Blog, Tags, HomePage,Author, YoutubeVideos
from random import randint
import random
from pygments import lexers
from pygments.formatters import HtmlFormatter
from pygments import highlight 
from pygments.styles import get_all_styles






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
  # formatter = HtmlFormatter(full=True, linenos=True,style=article.style)
  # lex =  lexers.get_lexer_by_name(article.language)
  # code = highlight(article.content, lex, formatter)
  
  youtube_links = YoutubeVideos.objects.all()[:4]
  related_articles = Blog.objects.filter(tag=article.tag.first())
  return render(request, 'blog/aticle-details.html', {'article':article ,
                                                      # 'result':code,
                                                      'youtube_links':youtube_links,
                                                      'related_articles':related_articles})


def article_list(request, tag):
  if tag == 'html':
    menu = '''
             <i style="color: #FD7E14;" class="fab fa-html5"></i>&nbsp;Html + 
             <i style="color: #82C91E;" class="fab fa-css3"></i>&nbsp;Css
           '''
  elif tag=='python':
    menu = '''
          <i style="color: #3471A1;" class="fab fa-python"></i>&nbsp; Python
          '''
  elif tag=='javascript':
    menu = ''' <i style="color: #EFD81D;" class="fab fa-js"></i> &nbsp; Javascript'''
  elif tag == 'django':
    menu = '''<i style="color: #FFD442;" class="fab fa-python"></i>&nbsp; Django '''
  if Tags.objects.filter(tag=tag).first()=='NoneType':
    tags = 0
  else:
    tags = Tags.objects.filter(tag=tag).first()
  article_list = Blog.objects.filter(tag=tags)
  youtube_links = YoutubeVideos.objects.all()[:4]
  recent_articles = Blog.objects.all().order_by('date')[:4]
  return render(request, 'blog/main-menu-article-list.html', {'all_articles':article_list,
                                                      'recent_articles':recent_articles,
                                                      'youtube_links':youtube_links,
                                                      'menu':menu})
