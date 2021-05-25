from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article-details/<str:slug>/', views.article_details, name='article_details'),
    path('article-list/', views.article_list, name='article_list'),
    path('article-list-tags/<str:tag>/', views.article_list_by_tag, name='article_list_by_tag'),
    path('search-website', views.search_form, name='search_form'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('postblog/', views.postblog, name='postblog'),

]