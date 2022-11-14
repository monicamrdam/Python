import requests

baseurl='https://rickandmortyapi.com/api/'
endpoint = 'character'

def main_request(baseurl, endpoint):
    r = requests.get(baseurl + endpoint)
    return r.json()



data = main_request(baseurl, endpoint)
#Lista de objetos
#Obtengo los datos de la páginas del caracter
pages = data['info']['pages']

#Obtengo lista de objetos del primer personaje
id = data['results'][0]['id']
name = data['results'][0]['name']
location = data['results'][0]['origin'] ['url']
episodes = data['results'][0]['episode']


#Función para imprimir los datos
def printDate():
    print(id)
    print(name)
    print(location)
    print(episodes)
    print('###########################################')

#Función para obtener los datos de cada personaje
#Cantidad de personajes
lenCharacters = (len(data['results']))
caracterlist=[]
for num in range(lenCharacters):
    #print(lenCharacters)
    id = data['results'][num]['id']
    name = data['results'][num]['name']
    location = data['results'][num]['origin']['url']
    episodes = data['results'][num]['episode']
    #printDate()
    #Creo una lista de objetos que me interesan obtener
    caracter={
        'id': id,
        'name':name,
        'location': location,
        'episode': episodes,
    }
    caracterlist.append(caracter)

print(caracterlist)








