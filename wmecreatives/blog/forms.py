from django.db import models
from django.forms import ModelForm , Textarea
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

