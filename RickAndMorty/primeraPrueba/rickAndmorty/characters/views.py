from django.http import HttpResponse
from django.http import JsonResponse

import requests

def index(request):
    response = requests.get("https://rickandmortyapi.com/api/character"
                            "")
    print(response.status_code)

    if response.status_code != 200:
        return HttpResponse('ERROR GET ' + WEATHER_API_URL + ' {}'.format(resp.status_code))
    else:
        print(response.json())
    return JsonResponse(response.json())



