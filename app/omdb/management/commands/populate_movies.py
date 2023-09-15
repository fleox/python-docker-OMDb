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
        star_wars_actors = [
            "Mark Hamill",
            "Harrison Ford",
            "Carrie Fisher",
            "Alec Guinness",
            "Ewan McGregor",
            "Natalie Portman",
            "Hayden Christensen",
            "Liam Neeson",
            "Samuel L. Jackson",
            "Anthony Daniels",
            "Kenny Baker",
            "Peter Mayhew",
            "James Earl Jones",
            "David Prowse",
            "Billy Dee Williams",
            "Frank Oz",
            "Ian McDiarmid",
            "Christopher Lee",
            "Adam Driver",
            "Daisy Ridley",
            "John Boyega",
            "Oscar Isaac",
            "Gwendoline Christie",
            "Domhnall Gleeson",
            "Felicity Jones",
            "Diego Luna",
            "Forest Whitaker",
            "Donnie Yen",
            "Ben Mendelsohn",
            "Alan Tudyk",
            "Kelly Marie Tran",
            "Laura Dern",
            "Benicio Del Toro",
            "Lupita Nyong'o",
            "Warwick Davis",
            "Billie Lourd"
        ]
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
                
                # check if actor Paul Walker play in this movie
                if "Paul Walker" in actors_list:
                    k['withPaulWalker'] = True

                # find star-war actor in this movie
                actorsCommonStarWars = ""
                for item in star_wars_actors:
                    # Check if the element is also in list2
                    if item in actors_list:
                        actorsCommonStarWars=actorsCommonStarWars+item+", "
                
                k['actorsCommonStarWars'] = actorsCommonStarWars

                movie, created = Movie.objects.get_or_create(**k)

                for name in actors_list:
                    actor, created = Actor.objects.get_or_create(name=name)
                    movie.actor.add(actor)

                movie.save()
                print(movie)