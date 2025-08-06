from django.apps import AppConfig


class DjangoModels2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_models_2'

    def ready(self):
        import django_models_2.signals
