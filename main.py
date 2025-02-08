import os
import sys
import qdarkstyle
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from rest_url import api_request
from main_ui import Ui_MainWindow as main_ui
from about_window import AboutWindow

class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #darkstyle
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

        #button
        self.pokemon_name.returnPressed.connect(self.pokemon_get)

        #menubar
        self.actionAbout.triggered.connect(self.show_about)
        self.actionAbout_Qt.triggered.connect(self.about_qt)
        
    def pokemon_get(self):

        self.table1.setRowCount(0)
        self.table2.setRowCount(0)
        self.table3.setRowCount(0)

        os.system("CLS")

        pokemon_info = api_request(self.pokemon_name.text())

        name = pokemon_info["name"]

        self.pokemon_label.setText(name)

        print(f"Name: {pokemon_info["name"]}")
        print(f"Weight: {pokemon_info["weight"]}")

        for row in range (0,500): # this is used to loop through all the available moves, i set it to 500 times and will cycle through as much and break out of it
            try:
                self.table1.setColumnCount(1)
                self.table1.setHorizontalHeaderLabels(['Moves'])
                self.table1.insertRow(row)
                moves = pokemon_info["moves"][row]["move"]["name"]
                self.table1.setItem(row, 0, QTableWidgetItem(moves))
                print(f"Move {row+1}: {pokemon_info["moves"][row]["move"]["name"]}")
                row +=1
            except IndexError:
                break

        for row in range (0,500): # this is used to loop through all the available abilities, i set it to 500 times and will cycle through as much and break out of it
            try:
                self.table2.setColumnCount(1)
                self.table2.setHorizontalHeaderLabels(['Abilities'])
                self.table2.insertRow(row)
                ability = pokemon_info["abilities"][row]["ability"]["name"]
                self.table2.setItem(row, 0, QTableWidgetItem(ability))
                print(f"Ability {row+1}: {ability}")
                row += 1
            except IndexError:
                break
            
            weight = pokemon_info["weight"]
            self.weight_label.setText(str(weight))

        print ("thank you")
        
        self.pokemon_name.clear()

    def about_qt(self):
        QApplication.aboutQt()

    def show_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())