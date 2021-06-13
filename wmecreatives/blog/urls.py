from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bloglist/', views.bloglist, name='bloglist'),
    path('blogdetail/', views. blogdetail, name=' blogdetail'),

]