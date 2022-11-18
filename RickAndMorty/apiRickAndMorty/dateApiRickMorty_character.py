import requests

baseurl='https://rickandmortyapi.com/api/'
endpoint = 'character'

"""
Llamada a la api
r = requests.get(baseurl + endpoint)
funciona la llamada
print(r)
Mostramos los resultados json
data = r.json()
Datos generales de la api
print(data ['info'])
___________________________________
Cantidad de character que tiene la api
countCharacters= data['info']['count']
print(isinstance(countCharacters, int))
Cantidad de páginas que tiene la api
pages = data['info']['pages']

Datos de los character
___________________________________
nameCharacters = data['results'][0]['name']
locationCharacters = data['results'][0]['location']['name']
episodesCharacters=data['results'][0]['episode']
lenEpisodesCharacters=len(episodesCharacters)
print(nameCharacters)
print(locationCharacters)
print(lenEpisodesCharacters)

Accedemos a los datos
nameCharacters = charactersData['results'][0]['name']
locationCharacters = charactersData['results'][0]['location']['name']
episodesCharacters = charactersData['results'][0]['episode']
lenEpisodesCharacters = len(episodesCharacters)



Mostramos los datos para cada character  de id, name, location, episode
  characterOne = {
            'id': i['id'],
            'name': i['name'],
            'location': i['location']['name'],
            'episode': i['episode']
        }
        Añadimos los objetos dentro de la lista
        listChararcters.append(characterOne)
        return listChararcters
        """


#Función principal de la llamada a la Api, servira para obtener el número de páginas
def main_request(baseurl, endpoint):
    r = requests.get(baseurl + endpoint)
    return r.json()

#Función principal de la llamada a la API, sirvira para obtener todos los datos
def main_requestPath(path):
    r = requests.get(path)
    return r.json()

#Función para llamar a las páginas
def getPages(pages):
    numPages = pages['info']['pages']
    return  numPages

data = main_request(baseurl, endpoint)
numPagesApi = getPages(data)
print(numPagesApi)
print('==============================')


#Función para obtener los datos de los characters para cada página
def getCharactersData(charactersData):
    listChararcters =[]
    for i in charactersData['results']:
        char={
            'id': (i['id']),
            'name': (i['name']),
            'location' : (i['location']['name']),
            'episode': (i['episode']),

        }
        listChararcters.append(char)
    return listChararcters

#print(len(getCharactersData(data)))
#print(getCharactersData(data))


#Función para obtener todas las rutas de las paginas a las que hay llamar
#"https://rickandmortyapi.com/api/character?page=3"
def list_all_characters_pages(baseurl, endpoint):
    #empieza la api en la pagina 1 y termina en la 42
    numeroPage=(getPages(data))+1
    pageList=[]
    for i in range(1,numeroPage):
        path = (baseurl + endpoint + '?page='+str(i))
        pageList.append(path)
    return pageList

#Función para obtener todos los characters
def list_all_characters():
    caracterlist = []
    all_characters_pages = list_all_characters_pages(baseurl, endpoint)
    for path in all_characters_pages:
        dataPath = main_requestPath(path)
        caracterlist.extend(getCharactersData(dataPath))
    return caracterlist
