from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bloglist/', views.bloglist, name='bloglist'),
    path('blogdetail/<slug:slug>/', views.blogdetail, name='blogdetail'),
    # admin
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('post_blog/', views.post_blog, name='post_blog'),
    path('youtube_admin_sidebar/', views.youtube_admin_sidebar, name='youtube_admin_sidebar'),
    path('dailycode_admin_sidebar/', views.dailycode_admin_sidebar, name='dailycode_admin_sidebar'),
    path('allblogs_admin_sidebar/', views.BlogListView.as_view(), name='allblogs_admin_sidebar'),
    path('siteanalysis_admin_sidebar/', views.siteanalysis_admin_sidebar, name='siteanalysis_admin_sidebar'),
    path('comments_admin_sidebar/', views.comments_admin_sidebar, name='comments_admin_sidebar'),
    path('messages_admin_sidebar/', views.messages_admin_sidebar, name='messages_admin_sidebar'),
    path('subscriptions_admin_sidebar/', views.subscriptions_admin_sidebar, name='subscriptions_admin_sidebar'),
    path('users_admin_sidebar/', views.users_admin_sidebar, name='users_admin_sidebar'),
    path('settings_admin_sidebar/', views.settings_admin_sidebar, name='settings_admin_sidebar'),
    path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
    # comments
    path('save_comment/', views.save_comment, name='save_comment'),
    path('like_dislike_comment/<str:val>/<int:comment_id>/', views.like_dislike_comment, name='like_dislike_comment'),
    # contacts
    path('sendmessage/', views.sendmessage, name='sendmessage'),
    path('contacts/', views.contacts, name='contacts',)


]