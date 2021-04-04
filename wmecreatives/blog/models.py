from django.db import models

# Create your models here.

class HomePage(models.Model):
    site_theme = models.CharField(max_length=300, null=True, blank=True)
    video = models.FileField(upload_to='media_files/homepage/background_video')


    def __str__(self):
        return self.site_theme


class Author(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='media_files/authorImg')

    def __str__(self):
        return self.name

class Tags(models.Model):
    tag = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.tag

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
    lead_img = models.ImageField(upload_to='media_files/blog')
    date = models.DateField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    num_views = models.CharField(max_length=30, null=True, blank=True)
    read_time = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.title



class YoutubeVideos(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.link
