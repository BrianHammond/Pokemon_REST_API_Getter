try: 
    import requests
except ModuleNotFoundError: # if it's not then it will automatically be installed
    print("requests module is not installed")
    import subprocess
    required_packages = ['requests']
    for package in required_packages:
        subprocess.call(['pip', 'install', package])

import requests

def api_request(pokemon_name):
    
    base_url = "https://pokeapi.co/api/v2/"

    url=f"{base_url}pokemon/{pokemon_name}"

    if requests.get(url).status_code == 200:
        return requests.get(url).json()
    else:
        print(f"connection is bad {requests.get(url).status_code}")
