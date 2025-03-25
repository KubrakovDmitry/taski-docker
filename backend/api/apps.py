"""Модуль настройки приложения API."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Класс настройки API."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
