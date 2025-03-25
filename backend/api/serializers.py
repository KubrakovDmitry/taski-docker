"""Модуль сериализатора."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Класс серализатора."""

    class Meta:
        """Класс для настройки серализатора."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
