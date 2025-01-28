import requests

def get_pokemon_info(pokemon_name):
    
    base_url = "https://pokeapi.co/api/v2/"

    url=f"{base_url}pokemon/{pokemon_name}"

    if requests.get(url).status_code == 200:
        return requests.get(url).json()
    else:
        print(f"connection is bad {requests.get(url).status_code}")