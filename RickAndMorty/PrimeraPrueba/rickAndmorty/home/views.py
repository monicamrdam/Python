from django.http import HttpResponse


def index(request):
        return HttpResponse(
        'Hola Mundo. <br><br>Esto es una prueba de aplicación '
        'web con Django por <a href="https://proyectoa.com">Proyecto A</a>')