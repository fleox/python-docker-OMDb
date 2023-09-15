from rest_framework import serializers
from .models import Movie, Actor


class ActorSerializer(serializers.ModelSerializer):
    """
    Serializer for Actor model
    """
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model
    """
    actor = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('name', 'year', 'poster', 'director', 'actor')