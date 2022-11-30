import requests
from .character_client import Characters, Episodes
import re

baseurl='https://rickandmortyapi.com/api/'
endpointCharacter = 'character'
endpointEpisode = 'episode'


#Obtenemos el número de pagínas que hay en la api
def main_path(baseurl, endpoint):
    r = requests.get(baseurl + endpoint)
    return r.json()



numPageCharacter= main_path(baseurl,endpointCharacter)['info']['pages']
numCharacter=main_path(baseurl,endpointCharacter)['info']['count']
print(numPageCharacter)
print(numCharacter)
numPageEpisode= main_path(baseurl,endpointEpisode)['info']['pages']


dicEpisodeDic = {}
#Función para obtener los episodes de la api y guardarlos en un diccionario
def path_dataEpisode(baseurl, endpoint,numPage):
    for i in range(1, numPage + 1):
        path = (baseurl + endpoint + '?page=' + str(i))
        r = requests.get(path)
        dataEpsisode=r.json()
        for j in dataEpsisode['results']:
            episode = Episodes(
                id=(j['id']),
                name=(j['name']),
                air_date=(j['air_date']),
                episode=(j['episode']),
            )
            dicEpisodeDic = {
                'id': episode.id,
                'name': episode.name,
                'air_date': episode.air_date,
                'episode': episode.episode,
            }
            #print(dicEpisodeDic)
    return


path_dataEpisode(baseurl,endpointEpisode,numPageEpisode)





listChararcters = []
dicCharacters=[]
def path_dataCharacter(baseurl, endpoint,numPageCharacter):
    for i in range(1, numPageCharacter + 1):
        pathChaaracter = (baseurl + endpoint + '?page=' + str(i))
        r = requests.get(pathChaaracter)
        dataCharacter=r.json()
        for j in dataCharacter['results']:
            character=Characters (
                id=(j['id']),
                name=(j['name']),
                location=(j['location']['name']),
                numEpisode=len((j['episode'])),
                episode=(j['episode']),
            )
            char = {
                'id': character.id,
                'name': character.name,
                'location': character.location,
                'numEpisode': character.numEpisode,
                'episode': character.episode,
            }
            listChararcters.append(char)
    return

path_dataCharacter(baseurl,endpointCharacter,numPageCharacter)

#Falta por comparar los diccionarios para evitar llamadas a la api usando la funcion buscar diccionario