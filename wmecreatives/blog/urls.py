from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bloglist/', views.bloglist, name='bloglist'),
    path('blogdetail/<slug:slug>/', views.blogdetail, name='blogdetail'),
    # admin
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('post_blog/', views.post_blog, name='post_blog'),

]