from django.urls import path
from django.urls.conf import include, include
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'photos/', views.Photos_collectionsViewSet)

urlpatterns = [
    path('photos_api/',  views.images_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('images/', views.image_api, name='image_api'),


]