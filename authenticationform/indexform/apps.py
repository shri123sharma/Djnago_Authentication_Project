from django.apps import AppConfig

class IndexformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'indexform'
    def ready(self):
        import indexform.signals