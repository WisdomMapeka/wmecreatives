from django.shortcuts import render, get_object_or_404
from . models import Blog, Tags, HomePage,Author, YoutubeVideos
from random import randint
import random
from pygments import lexers
from pygments.formatters import HtmlFormatter
from pygments import highlight 
from pygments.styles import get_all_styles
from . forms import BlogForm






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
  related_articles = Blog.objects.filter(tag=article.tag.first())[:3]
  return render(request, 'blog/aticle-details.html', {'article':article ,
                                                      # 'result':code,
                                                      # 'content':article.content,
                                                      'youtube_links':youtube_links,
                                                      'related_articles':related_articles})


def article_list(request):
  menu = '''
          <i class="fas fa-list"></i>
          &nbsp; All Articles
          '''
  article_list = Blog.objects.all()
  youtube_links = YoutubeVideos.objects.all()[:4]
  recent_articles = Blog.objects.all().order_by('date')[:4]
  return render(request, 'blog/main-menu-article-list.html', {'all_articles':article_list,
                                                      'recent_articles':recent_articles,
                                                      'youtube_links':youtube_links,
                                                      'menu':menu})


def article_list_by_tag(request, tag):
  if Tags.objects.filter(tag=tag).exists():
    if Tags.objects.get(tag=tag).icon_class is not None:
        tag_name = Tags.objects.get(tag=tag)
        menu = str(tag_name.icon_class) + "&nbsp;" + str(tag_name)
    else:
        tag_name = Tags.objects.get(tag=tag)
        menu = "&nbsp;" + str(tag_name)
  tag_id = Tags.objects.filter(tag=tag).first()
  article_list = Blog.objects.filter(tag=tag_id)
  youtube_links = YoutubeVideos.objects.all()[:4]
  recent_articles = Blog.objects.all().order_by('date')[:4]
  return render(request, 'blog/main-menu-article-list.html', {'all_articles':article_list,
                                                      'recent_articles':recent_articles,
                                                      'youtube_links':youtube_links,
                                                      'menu':menu})



def search_form(request):
  recent_articles = Blog.objects.all().order_by('date')[:4]
  all_articles = Blog.objects.all()
  youtube_links = YoutubeVideos.objects.all()[:4]
  return render(request, 'blog/search-templates/search_form.html', {'all_articles':all_articles ,
                                                   'recent_articles':recent_articles,
                                                    # 'result':code,
                                                    'youtube_links':youtube_links})


def dashboard(request):
  return render(request, 'blog/dashboard/index.html')

def postblog(request):
  # form = BlogForm()
  tags = Tags.objects.all()
  author = Author.objects.all()

  if request.method == 'POST':
    title = request.POST.get('title', None)
    slug = request.POST.get('slug', None)
    num_views = request.POST.get('num-views', None)
    read_time = request.POST.get('read-time', None)
    tag = request.POST.get('tag', None)
    language = request.POST.get('Language', None)
    image = request.FILES.get('image', None)
    summary = request.POST.get('summary', None)
    content = request.POST.get('content', None)
    

    blog = Blog(title=title,
                               summary=summary,
                               content=content,
                               num_views=num_views, 
                               read_time=read_time, 
                               language=language,
                               lead_img=image)
    blog.save()
    blog.tag.add(tag)
    
    print(request.POST)
    print(request.FILES)
  return render(request, 'blog/dashboard/form-elements-component.html', {'tags':tags,
                                                                         'author':author})

