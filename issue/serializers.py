from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    content = serializers.CharField(max_length=10)
    type = serializers.IntegerField(default=1)

    class Meta:
        model = Task
        fields = ['title', 'content', 'type', 'created_at', 'updated_at']

# class TaskSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField(max_length=10)
#     type = serializers.IntegerField(default=1)