# RESTful API Requests
# to install run 'pip install requests'

try: # checks to see if the 'requests' module is installed
    from PyQt6.QtWidgets import QMainWindow, QApplication
    from PyQt6 import uic
except ModuleNotFoundError: # if it's not then it will automatically be installed
    print("The requests module is not installed")
    import subprocess
    required_packages = ['requests', 'PyQT6']
    for package in required_packages:
        subprocess.call(['pip', 'install', package])

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
import os
from api import get_pokemon_info

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        
        self.pokemon_name.returnPressed.connect(self.pokemon_get)

    def pokemon_get(self):

        os.system("CLS")
              
        pokemon_name = self.pokemon_name.text()

        get_pokemon_info(pokemon_name)
                     
        print(f"Name: {get_pokemon_info(pokemon_name)["name"]}")
        print(f"Weight: {get_pokemon_info(pokemon_name)["weight"]}")

        for x in range (0,500): # this is used to loop through all the available abilities, i set it to 500 times and will cycle through as much and break out of it
            try:
                get_pokemon_info(pokemon_name)["abilities"][x]["ability"]["name"]
                print(f"Ability {x+1}: {get_pokemon_info(pokemon_name)["abilities"][x]["ability"]["name"]}")
                x +=1
            except IndexError:
                break

        for x in range (0,500): # this is used to loop through all the available moves, i set it to 500 times and will cycle through as much and break out of it
            try:
                get_pokemon_info(pokemon_name)["moves"][x]["move"]["name"]
                print(f"Move {x+1}: {get_pokemon_info(pokemon_name)["moves"][x]["move"]["name"]}")
                x +=1
            except IndexError:
                break
        print ("thank you")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    UIWindow.show()
    sys.exit(app.exec())