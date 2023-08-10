from django.urls import path, include

from Fitness_store.fitness_app.views import HomePageView, AboutUsPageView, SupplementsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsPageView.as_view(), name='about us'),
    path('supplements', SupplementsPageView.as_view(), name='supplements')
]
