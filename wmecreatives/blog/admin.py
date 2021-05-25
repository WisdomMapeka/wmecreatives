from django.contrib import admin
from . models import Blog, Tags, HomePage,Author, YoutubeVideos

# Register your models here.
admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(Author)
admin.site.register(HomePage)
admin.site.register(YoutubeVideos)
# admin.site.register(Menu)



# class BlogAdmin(admin.ModelAdmin):
#     class Media:
#         js = ('https://cdn.quilljs.com/1.3.6/quill.js',
#             'blog/dashboard-assets/current/js/custom_admin.js',

#               )    
#         css = {
#              'all': ('blog/dashboard-assets/current/css/custom_admin.css',
#                      'blog/dashboard-assets/current/css/quill.snow.css')
#         }
# admin.site.register(Blog, BlogAdmin)