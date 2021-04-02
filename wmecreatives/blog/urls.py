from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article_details/<str:slug>/', views.article_details, name='article_details'),
    path('article_list/<str:tag>/', views.article_list, name='article_list'),

]