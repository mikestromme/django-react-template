"""
Global URL Configuration: The project-level urls.py file is where you define global URL patterns that apply to the entire project. 
These might include URLs for the project's homepage, authentication views, or any other views that are not specific to a particular app.

Including App-Specific URLs: The project-level urls.py file is where you include the URL patterns from each individual app. 
This allows you to organize your project's URLs in a modular way, with each app contributing its own set of URL patterns.

Namespacing: Similar to the urls.py file within an app, you can namespace your project-level URL patterns. Namespacing helps avoid 
naming conflicts between different apps and provides a way to organize URLs.

"""

# when site is launched this is the first place the code will look

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # called routes
    path('', include('api.urls'))
]


# localhost:8000/admin
# localhost:8000/ shows the views at api.urls
