from django.urls import path, include

from Fitness_store.fitness_app.views import the_view

urlpatterns = [
    path('', the_view)
]
