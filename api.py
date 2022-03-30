import requests
import json

def api(ciudad):
    url = f'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20{ciudad}%20&limit=50'
    response = requests.get(url)
    data = response.json()

    json = data["results"]

    return json

