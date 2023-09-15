import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.shortcuts import render
from omdb import models


def spreadsheet_upload(request):

    context = {}
    movies = models.Movie.objects.filter(name__contains='Pirates')
    context['movies'] = movies

    credentials = {
        "type": "service_account",
        "project_id": "",
        "private_key_id": "",
        "private_key": "",
        "client_email": "",
        "client_id": "",
        "auth_uri": "",
        "token_uri": "",
        "auth_provider_x509_cert_url": "",
        "client_x509_cert_url": ""
    }

    gc = gspread.service_account_from_dict(credentials)

    data_to_update = [
        ["name", "year", "poster", "director", "producedBefore2015", "withPaulWalker", "actorsCommonStarWars"],
    ]

    for movie in movies:
        t_movie = [movie.name, movie.year, movie.poster, movie.director, movie.producedBefore2015, movie.withPaulWalker, movie.actorsCommonStarWars] 
        data_to_update.append(t_movie) 

    sh = gc.open("movies")
    sh.sheet1.update('A1', data_to_update)
    
    return render(request, "upload.html", context)
