"""  
Request Handling: Views are responsible for handling incoming HTTP requests. When a user interacts with a Django web application by visiting a URL
, the associated view function in views.py is called to process the request.

Business Logic: Views contain the business logic of the application. This is where you define the actions that need to be taken based on the 
user's input. This may involve querying a database, processing data, and performing various operations.

HTTP Responses: Views are responsible for generating HTTP responses that are sent back to the user's browser. This includes rendering HTML content
, redirecting to other URLs, or returning JSON data for API endpoints.

Template Rendering: For web applications that use templates, views are often responsible for rendering these templates. Templates are used to generate
dynamic HTML content by combining static HTML with data from the views.

Class-Based Views: While Django supports function-based views, it also provides class-based views for a more organized and reusable code structure. 

Class-based views allow you to encapsulate related functionality within a class, making it easier to extend and customize views.
"""



from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.response import Response
from .models import *


# def home(request): 
#     return HttpResponse("This is the homepage")
class ProjectManagerViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = ProjectManager.objects.all()
    serializer_class = ProjectManagerSerializer

    def list(self, request):
        queryset = ProjectManager.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ProjectViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request):
        queryset = Project.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project,data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)
        




