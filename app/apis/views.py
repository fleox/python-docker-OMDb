from rest_framework import generics

from omdb import models
from .serializers import MovieSerializer

class ListMovies(generics.ListCreateAPIView):
    allowed_methods = ['GET']
    queryset = models.Movie.objects.all()
    serializer_class = MovieSerializer

class ListMoviesFastFurious(generics.ListCreateAPIView):
    allowed_methods = ['GET']
    queryset = models.Movie.objects.filter(name__contains='Fast')
    serializer_class = MovieSerializer

class ListMoviesPiratesCaraibes(generics.ListCreateAPIView):
    allowed_methods = ['GET']
    queryset = models.Movie.objects.filter(name__contains='Pirates')
    serializer_class = MovieSerializer