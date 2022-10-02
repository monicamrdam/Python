from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'Hola Mundo. <br>Estos son los personajes de Rick and Morty<br>')