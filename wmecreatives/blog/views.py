from django.shortcuts import render, get_object_or_404
from . models import Blog, Tags, HomePage,YoutubeVideos, TodaysCode, Categories
import datetime



# Create your views here.
def index(request):
    today = datetime.date.today()
    home_record = HomePage.objects.all().first()
    todayscode = TodaysCode.objects.filter(date_created__gt = today).first()
    # change blogs later to query only the latest 4
    blogs = Blog.objects.all()[:4]
    categories = Categories.objects.all()
    # change youtube_vids later to query only the latest 4
    youtube_vids = YoutubeVideos.objects.all()[:4]
    return render(request, 'blog/index.html', {'home_record':home_record,
                                               'todayscode':todayscode,
                                               'blogs':blogs,
                                               'categories':categories,
                                               'youtube_vids':youtube_vids})

def bloglist(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/bloglist.html', {'blogs':blogs})

def blogdetail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog/blogdetail.html', {"blog":blog})

def admin_panel(request):
    return render(request, 'blog/admin_panel/admin_home.html')

def post_blog(request):
    if request.method == 'POST':
        title = request.POST.get('blog-title', None)
        slug = request.POST.get('blog-slug', None)
        lead_img = request.FILES.get('lead-img', None)
        blog_content = request.POST.get('blog-content', None)
        blog_summary = request.POST.get('blog-summary', None)
        author = request.POST.get('author', None)

        blog = Blog.objects.create(title=title, slug=slug, lead_img=lead_img, content=blog_content,
                                   summary=blog_summary, author=author)
        blog.save()



        # print(blog_content)
        # print(request.FILES)

    return render(request, 'blog/admin_panel/post_blog.html')
