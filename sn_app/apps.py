from django.apps import AppConfig

class SnAppConfig(AppConfig):
    name = 'sn_app'
    def ready(self):
        import signals