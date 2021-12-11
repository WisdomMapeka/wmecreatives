from django.shortcuts import render
from . models import Photos_collections
from .serializers  import Photos_collectionsSerializers 
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.

def image_api(request):
    photos = Photos_collections.objects.all()
    return render(request, "blog_api/image_api.html", {'photos':photos})





@csrf_exempt
def images_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        images = Photos_collections.objects.all()
        serializer = Photos_collectionsSerializers(images, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Photos_collectionsSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


