from __future__ import unicode_literals

from django.db import models

class Actor(models.Model):
    """
    Actor model : Table for movie Actors
    """
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    """
    Movie model : model for Movies
    """
    name = models.CharField(max_length=500)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    director = models.CharField(max_length=500)
    actor = models.ManyToManyField(Actor)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name