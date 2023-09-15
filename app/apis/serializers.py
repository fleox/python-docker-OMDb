from rest_framework import serializers
from omdb import models


class ActorSerializer(serializers.ModelSerializer):
    """
    Serializer for Actor model
    """
    class Meta:
        model = models.Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model
    """
    actor = ActorSerializer(many=True)

    class Meta:
        model = models.Movie
        fields = '__all__'