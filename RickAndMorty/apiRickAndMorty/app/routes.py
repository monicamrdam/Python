#importamos flask
from flask import Flask
#Importamos la libreria jsonify para convertir un objeto en un json
from flask import jsonify

from .character_service import listChararcters
#Creamos la aplicación de servidor
app = Flask(__name__)

#Creamos una ruta de prueba home para testear que el servidor funciona
@app.route('/home')
def home():
    return '!Bienvenido!'


#Importamos los datos de los character que hemos obtenido de la API
@app.route('/characters')
def getCharacters():
    #return listChararcters
    return jsonify(listChararcters)