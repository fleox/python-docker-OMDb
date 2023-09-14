import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from omdbapi.movie_search import GetMovie

import requests
from pprint import PrettyPrinter
pp = PrettyPrinter()

from ...models import Movie, Actor


class Command(BaseCommand):
    """
    store movies data from provided dump
    """
    def handle(self, *args, **options):

        apiKey = "98b330ef"

        #Fetch Movie Data with Full Plot 
        data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
        year = ''
        movie = 'Fast & Furious' 
        params = {
            's':movie,
            'type':'movie',
            'y':year,
            'plot':'full'
        }
        
        response = requests.get(data_URL,params=params).json()
        pp.pprint(response)