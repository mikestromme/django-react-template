"""
used to submit data from frontend to backend and vice versa

Data Serialization: Serializers define how data should be converted into a format that can be easily rendered into JSON or other content types. 
They provide a way to convert complex data structures, such as Django models, into Python data types that can be easily serialized and sent over the network.

Model Serialization: In the context of Django models, serializers are often used to convert model instances or querysets into a format that can be easily 
transmitted over the network. This is essential when building APIs, as clients expect data to be in a standardized format like JSON.

Data Validation: Serializers can also be used for data validation. When deserializing (converting incoming data to Python objects), serializers can check
whether the provided data is valid according to certain rules defined in the serializer class. This helps ensure that only valid data is processed by the application.

Handling Complex Relationships: Django models often have relationships with other models (e.g., ForeignKey or ManyToManyField). Serializers help manage 
and represent these relationships in a way that can be easily serialized and deserialized.
"""

from rest_framework import serializers
from .models import * 

class ProjectSerializer(serializers.ModelSerializer): # model class
    class Meta: 
        model = Project
        fields = ('id','name','projectmanager', 'start_date', 'end_date', 'comments', 'status')


class ProjectManagerSerializer(serializers.ModelSerializer): # model class
    class Meta: 
        model = ProjectManager
        fields = ('name', 'id')
 