
import unittest
import requests


#Creamos la clase Test
class TestAPI(unittest.TestCase):
    URL_CHARACTER ="http://127.0.0.1:2000/characters"

    first_data={
        "episodes": [
            "Pilot",
            "Lawnmower Dog",
            "Anatomy Park",
            "M. Night Shaym-Aliens!",
            "Meeseeks and Destroy",
            "Rick Potion #9",
            "Raising Gazorpazorp",
            "Rixty Minutes",
            "Something Ricked This Way Comes",
            "Close Rick-counters of the Rick Kind",
            "Ricksy Business",
            "A Rickle in Time",
            "Mortynight Run",
            "Auto Erotic Assimilation",
            "Total Rickall",
            "Get Schwifty",
            "The Ricks Must Be Crazy",
            "Big Trouble in Little Sanchez",
            "Interdimensional Cable 2: Tempting Fate",
            "Look Who's Purging Now",
            "The Wedding Squanchers",
            "The Rickshank Rickdemption",
            "Rickmancing the Stone",
            "Pickle Rick",
            "Vindicators 3: The Return of Worldender",
            "The Whirly Dirly Conspiracy",
            "Rest and Ricklaxation",
            "The Ricklantis Mixup",
            "Morty's Mind Blowers",
            "The ABC's of Beth",
            "The Rickchurian Mortydate",
            "Edge of Tomorty: Rick, Die, Rickpeat",
            "The Old Man and the Seat",
            "One Crew Over the Crewcoo's Morty",
            "Claw and Hoarder: Special Ricktim's Morty",
            "Rattlestar Ricklactica",
            "Never Ricking Morty",
            "Promortyus",
            "The Vat of Acid Episode",
            "Childrick of Mort",
            "Star Mort: Rickturn of the Jerri",
            "Mort Dinner Rick Andre",
            "Mortyplicity",
            "A Rickconvenient Mort",
            "Rickdependence Spray",
            "Amortycan Grickfitti",
            "Rick & Morty's Thanksploitation Spectacular",
            "Gotron Jerrysis Rickvangelion",
            "Rickternal Friendshine of the Spotless Mort",
            "Forgetting Sarick Mortshall",
            "Rickmurai Jack"
        ],
        "id": 1,
        "location": "Citadel of Ricks",
        "name": "Rick Sanchez"
    }

    last_data={
        "episodes": [
          "Rixty Minutes"
        ],
        "id": 20,
        "location": "Interdimensional Cable",
        "name": "Ants in my Eyes Johnson"
      }

    #Test 1 Verificamos que funciona el servidor
    def test_allData(self):
        resp=requests.get(self.URL_CHARACTER)
        #Comprobamos que se conecta
        self.assertEqual(resp.status_code, 200)
        #Comprobamos que son 20 caracteres
        self.assertEqual(len(resp.json(),20))
        #Comprobamos que el primer dato obtenido es el correcto
        self.assertDictEqual(resp.__dict__, self.first_data)
        # Comprobamos que el ultimo dato obtenido es el correcto
        self.assertDictEqual(resp.__dict__, self.last_data)
        print("Test 1 completed")


    #Si no encuentro solución a buscar en todo el diccionario
    def test_FirstData(self):
        resp = requests.get(self.URL_CHARACTER + '/1')
        # Comprobamos que el primer dato obtenido es el correcto
        self.assertDictEqual(resp.__dict__, self.first_data)

    def test_LastData(self):
        resp = requests.get(self.URL_CHARACTER + '/20')
        # Comprobamos que el ultimo dato obtenido es el correcto
        self.assertDictEqual(resp.__dict__, self.last_data)


#Ejecutamos los test
if __name__== "__main__":
    tester = TestAPI()

    #Ejecutamos el primer test
    tester.test_allData()
    tester.test_FirstData()
    tester.test_LastData()