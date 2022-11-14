#importamos flask
from flask import Flask
#Importamos la libreria jsonify para convertir un objeto en un json
from flask import jsonify

#Creamos la aplicación de servidor
app = Flask(__name__)

#Creamos una ruta de prueba home para testear que el servidor funciona
@app.route('/home')
def home():
    return '!Bienvenido!'



#Importamos los datos de los character que hemos obtenido de la API
from service_apiRickMorty_character import caracterlist
@app.route('/characters')
def getCharacters():
    return jsonify(caracterlist)


#Importamos datos de los character segun su id, siendo una ruta dinámica en función de su id
@app.route('/characters/<int:id_character>')
def getProduct(id_character):
    #Obtenemos la lista de personajes
    idCharacterFound= [id for id in caracterlist
        if id['id'] == id_character]
    #validamos que los datos buscados existan
    if (id_character>0):
        return jsonify({'character': idCharacterFound[0]})
    return jsonify({'message': 'No existe ese character'})




#Inicializamos el servidor
if __name__ =='__main__':
    #modo debug hace que el script ante los cambios se reinicie
    #puerto en el que escucha el servidor sera el 2000
    app.run(debug=True, port=2000)
