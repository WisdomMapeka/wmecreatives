from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article-details/<str:slug>/', views.article_details, name='article_details'),
    path('article-list/<str:tag>/', views.article_list, name='article_list'),
    path('search-website', views.search_form, name='search_form'),

]