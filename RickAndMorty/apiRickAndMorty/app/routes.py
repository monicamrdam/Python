#importamos flask
from flask import Flask
#Importamos la libreria jsonify para convertir un objeto en un json
from flask import jsonify

from .controller import list_all_characters

#Creamos la aplicación de servidor
app = Flask(__name__)

#Creamos una ruta de prueba home para testear que el servidor funciona
@app.route('/home')
def home():
    return '!Bienvenido!'


#Importamos los datos de los character que hemos obtenido de la API
@app.route('/characters')
def getCharacters():
    return list_all_characters
    #return jsonify(list_all_characters())
