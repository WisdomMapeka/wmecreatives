from django.contrib import admin
from . models import Blog, Tags, HomePage,Author, YoutubeVideos

# Register your models here.
admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(Author)
admin.site.register(HomePage)
admin.site.register(YoutubeVideos)
