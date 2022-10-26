
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

c3=Caracter_Listas(3,"Summer Smith", "Human", "Female", "https://rickandmortyapi.com/api/location/20")
c1=Caracter_Listas(1,"Rick Sanchez", "Human", "Male", "https://rickandmortyapi.com/api/location/1")
c4=Caracter_Listas(4,"Beth Smith", "Human", "Female", "https://rickandmortyapi.com/api/location/20")
c2=Caracter_Listas(2,"Morty Smith", "Human", "Male", "")




lista_cacacter= [ c3, c1, c4, c2 ]
#https://docs.python.org/es/3/howto/sorting.html
sorted(lista_cacacter, key=lambda Caracter_Listas: Caracter_Listas.id)
for caracter in lista_cacacter:
  print (caracter)