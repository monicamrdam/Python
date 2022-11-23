import requests
import pandas as pd
baseurl='https://rickandmortyapi.com/api/'
endpoint = 'character'

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
    listEpidose=[]
    nameEpisode = []
    for i in charactersData['results']:
        listEpidose.extend((i['episode']))
        for path in listEpidose:
            dataEpisode =main_requestPath(path)
            #print (dataEpisode['name'])
            nameEpisode=(dataEpisode['name'])
        char = {
            'id': (i['id']),
            'name': (i['name']),
            'location': (i['location']['name']),
            'numEpisode': len((i['episode'])),
            'episode': (i['episode']),
            'nameEpisode': nameEpisode,
        }
        listChararcters.append(char)

    return listChararcters


#Función para obtener todas las rutas de las paginas a las que hay llamar
#"https://rickandmortyapi.com/api/character?page=3"
def list_all_characters_pages(baseurl, endpoint):
    #empieza la api en la pagina 1 y termina en la 42
    numeroPage=(getPages(data))+1
    pageList=[]
    for i in range(5,6):
        path = (baseurl + endpoint + '?page='+str(i))
        print(path)
        pageList.append(path)
    return pageList

def list_all_characters():
    caracterlist = []
    all_characters_pages = list_all_characters_pages(baseurl, endpoint)
    for path in all_characters_pages:
        dataPath = main_requestPath(path)
        #print(dataPath)
        caracterlist.extend(getCharactersData(dataPath))
    return caracterlist

#print(list_all_characters())


#Extraer los datos a traves de libreria panda
df = pd.DataFrame(list_all_characters())
print(df.head(), df.tail())
df.to_csv('charlist.csv', index=False)