from django.urls import path, include

from Fitness_store.fitness_app.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view())
]
