list_all_characters = "HOla"

import requests


baseurl='https://rickandmortyapi.com/api/'
endpointCharacter = 'character'
endpointEpisode = 'episode'
#Obtenemos el número de pagínas que hay en la api

def main_path(baseurl, endpoint):
    r = requests.get(baseurl + endpoint)
    return r.json()
"""
print ('numero de page path episode')
print (main_path(baseurl,endpointEpisode)['info']['pages'])
print ('numero de page path characters')
print (main_path(baseurl,endpointCharacter)['info']['pages'])
"""


""" No borrar...obtengo datos de result
def path_data(baseurl, endpoint,numPage):
    caracterlist = {}
    dataList={}
    for i in range(1, numPage + 1):
        path = (baseurl + endpoint + '?page=' + str(i))
        print(path)
        r = requests.get(path)
        data=r.json()
        for j in data['results']:
           #LLamada a la api
            #print(j['id'])
            #print(j['name'])
           #Datos que guardo en mi aplicación
            idEpisode=(j['id'])
            nameEpisode=(j['name'])
            caracterlist[idEpisode] =nameEpisode
    print(caracterlist)
    print(len(caracterlist))
    return

numePageEp= main_path(baseurl,endpointEpisode)['info']['pages']
path_data(baseurl,endpointEpisode,numePageEp)
"""

#Función para obtener los episodes de la api y guardarlos en un diccionario
def path_dataEpisode(baseurl, endpoint,numPage):
    episodeDic = {}
    for i in range(1, numPage + 1):
        path = (baseurl + endpoint + '?page=' + str(i))
        print(path)
        r = requests.get(path)
        data=r.json()
        for j in data['results']:
           #LLamada a la api
            #print(j['id'])
            #print(j['name'])
           #Datos que guardo en mi aplicación
            idEpisode=(j['id'])
            nameEpisode=(j['name'])
            episodeDic[idEpisode] =nameEpisode
    print(episodeDic)
    print(len(episodeDic))
    return



def path_dataCharacter(baseurl, endpoint,numPageCharacter):
    caracterlist = {}
    for i in range(1, numPageCharacter + 1):
        pathChaaracter = (baseurl + endpoint + '?page=' + str(i))
        #print(pathChaaracter)
        r = requests.get(pathChaaracter)
        dataCharacter=r.json()
        for j in dataCharacter['results']:
           #LLamada a la api
            #print(j['id'])
            #print(j['name'])
           #Datos que guardo en mi aplicación
            nameEpisode=(j['name'])
            caracterlist[j] =(j['id'])
    print(caracterlist)
    print(len(caracterlist))
    return

numPageEpisode= main_path(baseurl,endpointEpisode)['info']['pages']
numPageCharacter= main_path(baseurl,endpointCharacter)['info']['pages']
print(numPageCharacter)
path_dataEpisode(baseurl,endpointEpisode,numPageEpisode)
path_dataCharacter(baseurl,endpointCharacter,numPageCharacter)

