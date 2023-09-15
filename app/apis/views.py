from rest_framework import generics

from omdb import models
from .serializers import MovieSerializer

class ListMovies(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = MovieSerializer