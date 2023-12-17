from django.contrib import admin
from .models import * 

# register each table in our model
admin.site.register(Project)
admin.site.register(ProjectManager)
