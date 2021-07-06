from django.contrib import admin
from . models import Blog, Tags, HomePage, YoutubeVideos,TodaysCode, Categories, Comments, Messages

# Register your models here.
admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(HomePage)
admin.site.register(YoutubeVideos)
admin.site.register(TodaysCode)
admin.site.register(Categories)
admin.site.register(Comments)
admin.site.register(Messages)

