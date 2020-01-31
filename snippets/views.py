from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# The root of our API is going to be a view 
# that supports listing all the existing snippets, 
# or creating a new snippet.
@csrf_exempt 
def snippet_list(request):
    #This is GET METHOD
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
        #THIS IS THE POST METHOD
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid(): #if the POST request data is valid for the serializer
            serializer.save() #then it saves itself as a valid object
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt #This view (controller) is to move in the data of individual snippets
def snippet_detail(request, pk):
    try: #Brings a snippet per PK
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    #GET that individual snippet
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    #Updates the specific snippet
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    #Deletes the snippet pk
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
