import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from omdbapi.movie_search import GetMovie

import requests
from pprint import PrettyPrinter
pp = PrettyPrinter()
import sys

from ...models import Movie, Actor


class Command(BaseCommand):
    """
    store movies data from provided dump
    """
    def handle(self, *args, **options):

        apiKey = "98b330ef"
        movieslist = ["Pirates of the Caribbean", "Fast & Furious", "Star-Wars"]
        for movieToFind in movieslist:
            print(movieToFind)

            #Fetch Movie Data with Full Plot 
            data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
            year = '' 
            params = {
                's':movieToFind,
                'type':'movie',
                'y':year,
                'plot':'full'
            }
            
            response = requests.get(data_URL,params=params).json()

            k = {}
            for movie_item in response['Search']:
                
                #Fetch Movie Data with Full Plot 
                data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
                params = {
                    'i':movie_item.get('imdbID'),
                }
                movie = requests.get(data_URL,params=params).json()
                #pp.pprint(movie)

                k['producedBefore2015'] = False
                if int(movie.get('Year')) < 2015:
                    k['producedBefore2015'] = True
                
                k['name'] = movie.get('Title')
                k['year'] = movie.get('Year')
                k['poster'] = movie.get('Poster')
                k['director'] = movie.get('Director')
                
                actors_list = movie.get('Actors').split(", ")
                k['withPaulWalker'] = False
                
                if "Paul Walker" in actors_list:
                    k['withPaulWalker'] = True

                movie, created = Movie.objects.get_or_create(**k)

                for name in actors_list:
                    actor, created = Actor.objects.get_or_create(name=name)
                    movie.actor.add(actor)

                movie.save()
                print(movie)