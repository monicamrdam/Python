import requests
import json

response = requests.get("https://rickandmortyapi.com/api/character"
                        "")
#print(response.status_code)

#print(response.json())

print(type(response.json()))

numero_array= len(response.json()['results'])
print(len(response.json()['results']))


for x in range(numero_array):
    print(x)
    print(response.json()['results'][x]['name'])
    print(response.json()['results'][x]['species'])
    print(response.json()['results'][x]['gender'])
    print(response.json()['results'][x]['origin']['url'])
    print("==================================")


