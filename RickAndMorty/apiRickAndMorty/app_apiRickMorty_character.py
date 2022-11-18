#importamos flask
from flask import Flask
#Importamos la libreria jsonify para convertir un objeto en un json
from flask import jsonify

from apiRickAndMorty.dateApiRickMorty_character import list_all_characters

#Creamos la aplicación de servidor
app = Flask(__name__)

#Creamos una ruta de prueba home para testear que el servidor funciona
@app.route('/home')
def home():
    return '!Bienvenido!'


@app.route('/characters')
def getCharacters():
    return jsonify(list_all_characters())

#Inicializamos el servidor
if __name__ =='__main__':
    #modo debug hace que el script ante los cambios se reinicie
    #puerto en el que escucha el servidor sera el 2000
    app.run(debug=True, port=2000)
