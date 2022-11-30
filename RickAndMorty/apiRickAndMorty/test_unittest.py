

#https://docs.python.org/es/3.9/library/unittest.html
import unittest
import requests


#Creamos la clase Test
class TestAPI(unittest.TestCase):
    URL_HOME ="http://127.0.0.1:2000/home"
    URL_CHARACTER ="http://127.0.0.1:2000/characters"

    #Test 1 Verificamos que funciona el servidor
    def test_1_Home(self):
        resp=requests.get(self.URL_HOME)
        self.assertEqual(resp.status_code, 200)
        print("Test 1 completed")

    #Test 2 Verificamos que funciona la ruta character
    def test_2_CharacterS(self):
        resp = requests.get(self.URL_CHARACTER)
        self.assertEqual(resp.status_code, 200)
        print("Test 2 completed")

    #Test 3 verificamos que hemos obtenido todos los datos
    def test_3_getAllCharacters(self):
        resp = requests.get(self.URL_CHARACTER)
        self.assertEqual(len(resp.json()), 825)
        print("Test 3 completed")






#Ejecutamos los test
if __name__== "__main__":
    tester = TestAPI()

    #Ejecutamos el primer test
    tester.test_1_Home()
    tester.test_2_CharacterS()
    tester.test_3_getAllCharacters()
