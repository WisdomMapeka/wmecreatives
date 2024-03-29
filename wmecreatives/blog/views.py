from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from . models import Blog, Tags, HomePage,YoutubeVideos, TodaysCode, Categories, Comments, Messages
import datetime
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import ListView



# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs':blogs})

def bloglist(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/bloglist.html', {'blogs':blogs})

def blogdetail(request, slug):

    blog = Blog.objects.get(slug=slug)
    url_path_styles = "blog/highlight/styles/{}".format(blog.styleshit)
    styleshit_url  = staticfiles_storage.url(url_path_styles)
    print(styleshit_url)
    # The following query will have to be fixed to query based on related tags
    related_articles =  Blog.objects.all().exclude(slug=slug)[:2]

    return render(request, 'blog/blogdetail.html', {"blog":blog, 
                                                    "related_articles":related_articles, 
                                                    "styleshit_url":styleshit_url})



def save_comment(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        comment = request.POST.get('actual_comment', None)
        blog_id = request.POST.get('blog_id', None)
        print(blog_id)
        
        blog = Blog.objects.get(id=blog_id)
        save_comment = Comments.objects.create(name=name, comment=comment, blog=blog)
        save_comment.save()

        mydict = {"name":name, "comment":comment, "blog_id":blog_id, "date_created":save_comment.date_created}
    print(save_comment.date_created)
    return JsonResponse(mydict)

def like_dislike_comment(request, val, comment_id):
    total = ''
    if val == 'like':
        comment = Comments.objects.get(id=comment_id)
        comment.likes +=1
        comment.save()
        total = comment.likes
    elif val == 'dislike':
        comment = Comments.objects.get(id=comment_id)
        comment.dislikes +=1
        comment.save()
        total = comment.dislikes
        print(val)
        print(comment)
    else:
        pass
    
    comment_like_dislike_details = {"total_like_dislike":total, "val":val, "comment_id":comment_id }
    print(total, val)
    return JsonResponse(comment_like_dislike_details)


def sendmessage(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        message = request.POST.get("message", None)
        
        user_message = Messages.objects.create(name=name, email=email, phone=phone, message=message)
        user_message.save()

    return render(request, 'blog/sendmessage.html')


def contacts(request):
    return render(request, 'blog/contacts.html')


# ADMIN PANEL VIEWS
def admin_panel(request):
    return render(request, 'blog/admin_panel/admin_home.html')

def post_blog(request):
    categories = Categories.objects.all()
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
    return render(request, 'blog/admin_panel/post_blog.html', {'categories':categories})

def edit_post(request, id):
    blog = Blog.objects.get(id=id)
    categories = Categories.objects.all()

    if request.method == 'POST':
        title = request.POST.get('blog-title', None)
        slug = request.POST.get('blog-slug', None)
        lead_img = request.FILES.get('lead-img', None)
        blog_content = request.POST.get('blog-content', None)
        blog_summary = request.POST.get('blog-summary', None)
        author = request.POST.get('author', None)

        blog = Blog.objects.get(id=id)
        
        blog.title=title
        blog.slug=slug
        blog.lead_img=lead_img
        blog.content=blog_content
        blog.ummary=blog_summary
        blog.author=author

        blog.save()
    return render(request, 'blog/admin_panel/edit_post.html', {'blog':blog,'categories':categories})


def youtube_admin_sidebar(request):
    return render(request, 'blog/admin_panel/youtube_admin_sidebar.html')

def dailycode_admin_sidebar(request):
    return render(request, 'blog/admin_panel/dailycode_admin_sidebar.html')

# def allblogs_admin_sidebar(request):
#     blogs = Blog.objects.all()
#     return render(request, 'blog/admin_panel/allblogs_admin_sidebar.html', {'blogs':blogs})

class BlogListView(ListView):
    paginate_by = 5
    model = Blog
    template_name = 'blog/admin_panel/allblogs_admin_sidebar.html'

def siteanalysis_admin_sidebar(request):
    return render(request, 'blog/admin_panel/siteanalysis_admin_sidebar.html')

def comments_admin_sidebar(request):
    return render(request, 'blog/admin_panel/comments_admin_sidebar.html')

def messages_admin_sidebar(request):
    return render(request, 'blog/admin_panel/messages_admin_sidebar.html')

def subscriptions_admin_sidebar(request):
    return render(request, 'blog/admin_panel/subscriptions_admin_sidebar.html')

def users_admin_sidebar(request):
    return render(request, 'blog/admin_panel/users_admin_sidebar.html')

def settings_admin_sidebar(request):
    return render(request, 'blog/admin_panel/settings_admin_sidebar.html')