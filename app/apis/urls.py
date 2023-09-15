from django.urls import path

from .views import ListMovies

urlpatterns = [
    path('', ListMovies.as_view()),
]