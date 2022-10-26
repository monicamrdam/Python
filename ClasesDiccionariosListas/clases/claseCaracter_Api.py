import requests
import json

response = requests.get("https://rickandmortyapi.com/api/character"
                        "")
# print(response.status_code)

# print(response.json())

print(type(response.json()))

numero_array = len(response.json()['results'])
print(len(response.json()['results']))


#función para evitar cadenas vacias
def es_cadena_no_vacia (valor):
    return isinstance (valor, (str))

#funcion para verificar que es un número
def es_numero(valor):
    return isinstance(valor, (int, float, complex))

#Creamos una clase para mostar cada personaje
class Caracter_Listas(object):

    #atributos id, name, species, gender, origin_url)
    def __init__(self, id, name ="*", species ="*", gender="*", origin_url="*"):
        # Necesitamos validar que id es un número
        if es_numero(id):
            self.id = id
        #Necesitamos validar que name, species, gender y origin_url sean cadenas no vacías
        if es_cadena_no_vacia(name):
            self.name = name
        else:
            raise TypeError("El nombre del personaje no puede estar vacio")

        if es_cadena_no_vacia(species):
            self.species = species
        else:
            raise TypeError("La especie del personaje no puede estar vacia")

        if es_cadena_no_vacia(gender):
            self.gender = gender
        else:
            raise TypeError("El genero del personaje no puede estar vacio")

        if es_cadena_no_vacia(origin_url):
            self.origin_url = origin_url
        else:
            raise TypeError("El origin_url del personaje no puede estar vacio")

    def __repr__(self):
        return repr((self.id, self.name, self.species,self.gender, self.origin_url))

"""
print(response.json()['results'][x]['id'])
    print(response.json()['results'][x]['name'])
    print(response.json()['results'][x]['species'])
    print(response.json()['results'][x]['gender'])
    print(response.json()['results'][x]['origin']['url'])
    print("==================================")
    
"""

for x in range(numero_array):


    id =response.json()['results'][x]['id']
    nombre=response.json()['results'][x]['name']
    species=response.json()['results'][x]['species']
    gender= response.json()['results'][x]['gender']
    origin_url=response.json()['results'][x]['origin']['url']

    Caracter_Listas(id, nombre, species, gender,origin_url )

print(Caracter_Listas)
