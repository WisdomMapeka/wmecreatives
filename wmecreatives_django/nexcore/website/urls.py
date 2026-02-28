"""URL patterns for the website app."""
from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
]
