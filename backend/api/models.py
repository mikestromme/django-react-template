"""
In Django, the models.py file is used to define the data models for your application. Models represent the 
structure and behavior of your application's data, and they are used to interact with the database.

Django's ORM allows you to interact with the database using Python objects rather than raw SQL queries. 
Models define a high-level API for database operations, making it easier to perform common tasks such as 
creating, querying, updating, and deleting records.

"""




from django.db import models

class ProjectManager(models.Model): 
    name = models.CharField(unique=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Project(models.Model): 
    name = models.CharField(unique=True, max_length=100)
    projectmanager = models.ForeignKey(ProjectManager, on_delete=models.CASCADE, blank=True, null=True)  # notice foreign key to Project Managers class
    start_date = models.DateField()
    end_date = models.DateField()
    comments = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
  
