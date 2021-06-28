from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from . models import Blog, Tags, HomePage,YoutubeVideos, TodaysCode, Categories, Comments
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
    # The following query will have to be fixed to query based on related tags
    related_articles =  Blog.objects.all().exclude(slug=slug)[:2]

    return render(request, 'blog/blogdetail.html', {"blog":blog, "related_articles":related_articles})

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
    return render(request, 'blog/sendmessage.html')


def contacts(request):
    return render(request, 'blog/contacts.html')
