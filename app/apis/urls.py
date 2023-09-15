from django.urls import path

from .views import ListMovies, ListMoviesFastFurious

urlpatterns = [
    path('', ListMovies.as_view()),
    path('films/', ListMoviesFastFurious.as_view()),
]