# LibraryProject/relationship_app/apps.py
from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        # import signals to ensure they are registered
        from . import signals  # noqa: F401
