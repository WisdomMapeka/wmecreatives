from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bloglist/', views.bloglist, name='bloglist'),
    path('blogdetail/<slug:slug>/', views.blogdetail, name='blogdetail'),
    # admin
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('post_blog/', views.post_blog, name='post_blog'),
    # comments
    path('save_comment/', views.save_comment, name='save_comment'),
    path('like_dislike_comment/<str:val>/<int:comment_id>/', views.like_dislike_comment, name='like_dislike_comment'),
    # contacts
    path('sendmessage/', views.sendmessage, name='sendmessage'),
    path('contacts/', views.contacts, name='contacts',)


]