from django.urls import path

from .views import ListMovies, ListMoviesFastFurious, ListMoviesPiratesCaraibes

urlpatterns = [
    path('', ListMovies.as_view()),
    path('films/', ListMoviesFastFurious.as_view()),
    path('films/pirates_caraibes/', ListMoviesPiratesCaraibes.as_view()),
]