from django.http import HttpResponse


def movies(request):
    return HttpResponse("Hello, world. You're at the polls index.")