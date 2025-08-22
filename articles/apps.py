from django.apps import AppConfig

class ArticlesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "articles"

    def ready(self):
        from . import signals  # noqa: F401  (ensure signal handlers are registered)
