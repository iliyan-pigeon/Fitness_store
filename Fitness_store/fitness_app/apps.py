from django.apps import AppConfig


class FitnessAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Fitness_store.fitness_app'

    def ready(self):
        import Fitness_store.fitness_app.signals
