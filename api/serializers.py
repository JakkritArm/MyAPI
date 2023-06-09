from rest_framework import serializers
from api.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta: # To identify the purposal of this task as what's the proposal of this task?
        model = Task # to converse
        fields = (
            "id",
            "title",
            "description",
            "date_created",
            "complete"
        )