# RESTful API Requests
# to install run 'pip install requests'

try: # checks to see if the 'requests' module is installed
    import requests
except ModuleNotFoundError: # if it's not then it will automatically be installed
    print("The requests module is not installed")
    import subprocess
    required_packages = ['requests']
    for package in required_packages:
        subprocess.call(['pip', 'install', package])

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon_name):
    url=f"{base_url}pokemon/{pokemon_name}"

    if requests.get(url).status_code == 200:
        return requests.get(url).json()
    else:
        print(f"connection is bad {requests.get(url).status_code}")

pokemon_name = input("enter pokemon name: ")

print(f"Name: {get_pokemon_info(pokemon_name)["name"]}")
print(f"Weight: {get_pokemon_info(pokemon_name)["weight"]}")
print(f"Ability: {get_pokemon_info(pokemon_name)["abilities"][0]["ability"]["name"]}")

for x in range (0,500): # this is used to loop through all the available moves, i set it to 500 times and will cycle through as much and break out of it
    try:
        get_pokemon_info(pokemon_name)["moves"][x]["move"]["name"]
        print(f"Move {x+1}: {get_pokemon_info(pokemon_name)["moves"][x]["move"]["name"]}")
        x +=1
    except IndexError:
        break
print ("thank you")