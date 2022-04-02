import requests
import json

def api(barrio):
    url = f'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20{barrio}%20'
    response = requests.get(url)
    data = response.json()

    json = data["results"]
    return json


