from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','name','description']


class AdminMailSendSerializer(serializers.Serializer):
    
    email = serializers.EmailField()