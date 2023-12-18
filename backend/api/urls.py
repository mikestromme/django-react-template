"""
URL Patterns: The primary purpose of urls.py is to define URL patterns for your Django project. URL patterns are mappings between 
URLs entered by users and the views that should handle those URLs. You define these patterns using regular expressions and associate 
them with specific view functions or class-based views.

URL Parameters: You can capture parameters from the URL using angle brackets and regular expressions. These captured parameters can 
be passed to your view functions for further processing.

Namespace and App-Specific URLs: urls.py allows you to organize your URL patterns into namespaces, making it easier to manage and 
avoid conflicts between different parts of your project or between different apps within a project.

Include Other URL Patterns: You can include URL patterns from other apps or modules in your project using the include function.
This allows you to organize your URL patterns in a modular way.

Reverse URL Matching: Django provides the reverse function, which allows you to generate a URL based on a view name and optional parameters. 
This is useful for creating URLs in templates or other parts of your code without hardcoding them.

"""



from django.urls import path 
from .views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project', ProjectViewset, basename='project')
router.register('projectmanager', ProjectManagerViewset, basename='projectmanager')
urlpatterns = router.urls


# urlpatterns = [
#     path('', home)
# ]