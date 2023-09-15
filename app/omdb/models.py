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
    year = models.IntegerField()
    poster = models.CharField(max_length=500)
    director = models.CharField(max_length=500)
    producedBefore2015 = models.BooleanField(default=False)
    withPaulWalker = models.BooleanField(default=False)
    actorsCommonStarWars = models.CharField(max_length=500, default="")
    actor = models.ManyToManyField(Actor)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name