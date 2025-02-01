# RESTful API Requests
# to install run 'pip install requests'

try: # checks to see if the 'requests' module is installed
    from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QTableWidgetItem
    from PyQt6 import uic
except ModuleNotFoundError: # if it's not then it will automatically be installed
    print("The requests module is not installed")
    import subprocess
    required_packages = ['requests', 'PyQT6']
    for package in required_packages:
        subprocess.call(['pip', 'install', package])

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt6 import uic
import os
from rest_url import api_request

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        
        self.pokemon_name.returnPressed.connect(self.pokemon_get)

        #menubar
        self.actionAbout.triggered.connect(self.about)

    def about(self):
        self.window = QWidget()
        uic.loadUi("about.ui", self.window) #load the UI file
        self.window.show()
        
    def pokemon_get(self):

        self.table.setRowCount(0)

        os.system("CLS")
              
        pokemon_info = api_request(self.pokemon_name.text())

        name = pokemon_info["name"]

        self.pokemon_label.setText(name)

        print(f"Name: {pokemon_info["name"]}")
        print(f"Weight: {pokemon_info["weight"]}")
        
        for row in range (0,500): # this is used to loop through all the available moves, i set it to 500 times and will cycle through as much and break out of it
            try:
                self.table.insertRow(row)
                moves = pokemon_info["moves"][row]["move"]["name"]
                self.table.setItem(row, 2, QTableWidgetItem(moves))
                print(f"Move {row+1}: {pokemon_info["moves"][row]["move"]["name"]}")
                row +=1
            except IndexError:
                break

        for row in range (0,500): # this is used to loop through all the available abilities, i set it to 500 times and will cycle through as much and break out of it
            try:
                ability = pokemon_info["abilities"][row]["ability"]["name"]
                self.table.setItem(row, 1, QTableWidgetItem(ability))
                print(f"Ability {row+1}: {ability}")
                row += 1
            except IndexError:
                break
            
        weight = pokemon_info["weight"]
        self.table.setItem(0, 0, QTableWidgetItem(str(weight)))

        print ("thank you")
        
        self.pokemon_name.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    UIWindow.show()
    sys.exit(app.exec())