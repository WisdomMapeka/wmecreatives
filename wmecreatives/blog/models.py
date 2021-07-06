from django.db import models
from django.db import models
from django.contrib.staticfiles.storage import staticfiles_storage

styles_shits = staticfiles_storage.listdir('blog/highlight/styles')

choices = [(s,s) for s in styles_shits[1]]
# Create your models here.

class HomePage(models.Model):
    site_theme = models.CharField(max_length=300, null=True, blank=True)
    theme_description = models.CharField(max_length=1000, null=True, blank=True)
    video = models.FileField(upload_to='media_files/homepage/background_video', null=True, blank=True)
    background_img = models.ImageField(upload_to='media_files/homepage/background_img/inner', null=True, blank=True)
    icon = models.ImageField(upload_to="media_files/homepage/icon", null=True, blank=True)
    icon_class = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.site_theme


class TodaysCode(models.Model):
    title = models.CharField(max_length=200, default="TODAY'S CODE", null=True, blank=True)
    code = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title



class Tags(models.Model):
    tag = models.CharField(max_length=200, null=True, blank=True)
    icon_class = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.tag

class Categories(models.Model):
    name = models.CharField(null=True, blank=True, max_length=300)
    icon = models.ImageField(upload_to="media_files/Categories/icon", null=True, blank=True)
    icon_class = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
# class Menu(models.Model):
#     menu_name = models.CharField(max_length=200, null=True, blank=True)
#     menu_icon_class = models.CharField(max_length=1000, null=True, blank=True)
#     menu_name_plus_icon_class = models.CharField(max_length=1000, null=True, blank=True)

#     def __str__(self):
#         return self.menu_name

class Blog(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)
    tag = models.ManyToManyField(Tags, blank=True)
    lead_img = models.ImageField(upload_to='media_files/blog', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    author_image = models.ImageField(upload_to='media_files/authorImg', null=True, blank=True)
    youtube_video_link = models.TextField(null=True, blank=True)
    num_views = models.CharField(max_length=30, null=True, blank=True)
    read_time = models.CharField(max_length=30, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    styleshit = models.CharField(max_length=100, null=True, blank=True, choices=choices, default="shades-of-purple.min.css")
    


    def __str__(self):
        return self.title


class Comments(models.Model):
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    name  = models.CharField(max_length=300, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    dislikes = models.IntegerField(default=0, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class YoutubeVideos(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    Tags = models.ManyToManyField(Tags, blank=True)


    def __str__(self):
        return self.link


class Messages(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=300, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.name and self.email and self.phone:
            return "Name: {}   email: {}   phone: {}".format(self.name, self.email, self.phone)
        elif self.name and self.email:
            return "Name: {}   email: {}".format(self.name, self.email)
        elif self.name:
            return self.name
        else:
            return "NO NAME"