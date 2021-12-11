from django.core.exceptions import MultipleObjectsReturned
from django.db import models

# Create your models here.
class Photos_collections(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    uploded = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    photographer = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to = "api_photos")

    def __str__(self):
        return self.name

