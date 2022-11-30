

import unittest
import requests


#Creamos la clase Test
class TestAPI(unittest.TestCase):
    URL_CHARACTER ="http://127.0.0.1:2000/characters"

    first_data= {
        "episode": [
          "https://rickandmortyapi.com/api/episode/1",
          "https://rickandmortyapi.com/api/episode/2",
          "https://rickandmortyapi.com/api/episode/3",
          "https://rickandmortyapi.com/api/episode/4",
          "https://rickandmortyapi.com/api/episode/5",
          "https://rickandmortyapi.com/api/episode/6",
          "https://rickandmortyapi.com/api/episode/7",
          "https://rickandmortyapi.com/api/episode/8",
          "https://rickandmortyapi.com/api/episode/9",
          "https://rickandmortyapi.com/api/episode/10",
          "https://rickandmortyapi.com/api/episode/11",
          "https://rickandmortyapi.com/api/episode/12",
          "https://rickandmortyapi.com/api/episode/13",
          "https://rickandmortyapi.com/api/episode/14",
          "https://rickandmortyapi.com/api/episode/15",
          "https://rickandmortyapi.com/api/episode/16",
          "https://rickandmortyapi.com/api/episode/17",
          "https://rickandmortyapi.com/api/episode/18",
          "https://rickandmortyapi.com/api/episode/19",
          "https://rickandmortyapi.com/api/episode/20",
          "https://rickandmortyapi.com/api/episode/21",
          "https://rickandmortyapi.com/api/episode/22",
          "https://rickandmortyapi.com/api/episode/23",
          "https://rickandmortyapi.com/api/episode/24",
          "https://rickandmortyapi.com/api/episode/25",
          "https://rickandmortyapi.com/api/episode/26",
          "https://rickandmortyapi.com/api/episode/27",
          "https://rickandmortyapi.com/api/episode/28",
          "https://rickandmortyapi.com/api/episode/29",
          "https://rickandmortyapi.com/api/episode/30",
          "https://rickandmortyapi.com/api/episode/31",
          "https://rickandmortyapi.com/api/episode/32",
          "https://rickandmortyapi.com/api/episode/33",
          "https://rickandmortyapi.com/api/episode/34",
          "https://rickandmortyapi.com/api/episode/35",
          "https://rickandmortyapi.com/api/episode/36",
          "https://rickandmortyapi.com/api/episode/37",
          "https://rickandmortyapi.com/api/episode/38",
          "https://rickandmortyapi.com/api/episode/39",
          "https://rickandmortyapi.com/api/episode/40",
          "https://rickandmortyapi.com/api/episode/41",
          "https://rickandmortyapi.com/api/episode/42",
          "https://rickandmortyapi.com/api/episode/43",
          "https://rickandmortyapi.com/api/episode/44",
          "https://rickandmortyapi.com/api/episode/45",
          "https://rickandmortyapi.com/api/episode/46",
          "https://rickandmortyapi.com/api/episode/47",
          "https://rickandmortyapi.com/api/episode/48",
          "https://rickandmortyapi.com/api/episode/49",
          "https://rickandmortyapi.com/api/episode/50",
          "https://rickandmortyapi.com/api/episode/51"
        ],
        "id": 1,
        "location": "Citadel of Ricks",
        "name": "Rick Sanchez",
        "numEpisode": 51
      }

    last_data= {
        "episode": [
          "https://rickandmortyapi.com/api/episode/9"
        ],
        "id": 826,
        "location": "Earth (Replacement Dimension)",
        "name": "Butter Robot",
        "numEpisode": 1
      }
    #Test 1 Verificamos que funciona el servidor
    def test_allData(self):
        resp = requests.get(self.URL_CHARACTER)
        response_json = resp.json()
        self.assertEqual(resp.status_code, 200, "Se conecta al servidor")
        self.assertEqual(len(response_json), 826, "Hay 826 characters")
        self.assertEqual(response_json[0], self.first_data, "El primero es Rick")
        self.assertDictEqual(response_json[825], self.last_data, "El ultimo es Ants in my Eyes Johnson")
        print('ok')





#Ejecutamos los test
if __name__== "__main__":
    tester = TestAPI()

    #Ejecutamos el primer test
    tester.test_allData()
