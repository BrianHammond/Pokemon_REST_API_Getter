import os
import sys
import qdarkstyle
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import QSettings
from rest_url import api_request
from main_ui import Ui_MainWindow as main_ui
from about_window import AboutWindow

class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = QSettings('settings.ini', QSettings.IniFormat)
        self.loadSettings()

        #button
        self.le_pokemon_name.returnPressed.connect(self.pokemon_get)

        #menubar
        self.actionDarkMode.toggled.connect(self.dark_mode)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionAbout_Qt.triggered.connect(self.about_qt)

    def pokemon_get(self):
        self.table1.setRowCount(0)
        self.table2.setRowCount(0)
        self.table3.setRowCount(0)

        os.system("CLS")

        pokemon_name = api_request(self.le_pokemon_name.text())

        name = pokemon_name["name"]

        self.pokemon_label.setText(name)

        print(f"Name: {pokemon_name["name"]}")
        print(f"Weight: {pokemon_name["weight"]}")

        for row in range (0,500): # this is used to loop through all the available moves, i set it to 500 times and will cycle through as much and break out of it
            try:
                self.table1.setColumnCount(1)
                self.table1.setHorizontalHeaderLabels(['Moves'])
                self.table1.insertRow(row)
                moves = pokemon_name["moves"][row]["move"]["name"]
                self.table1.setItem(row, 0, QTableWidgetItem(moves))
                print(f"Move {row+1}: {pokemon_name["moves"][row]["move"]["name"]}")
                row +=1
            except IndexError:
                break

        for row in range (0,500): # this is used to loop through all the available abilities, i set it to 500 times and will cycle through as much and break out of it
            try:
                self.table2.setColumnCount(1)
                self.table2.setHorizontalHeaderLabels(['Abilities'])
                self.table2.insertRow(row)
                ability = pokemon_name["abilities"][row]["ability"]["name"]
                self.table2.setItem(row, 0, QTableWidgetItem(ability))
                print(f"Ability {row+1}: {ability}")
                row += 1
            except IndexError:
                break
            
            weight = pokemon_name["weight"]
            self.weight_label.setText(str(weight))

        print ("thank you")
        
        self.le_pokemon_name.clear()

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def about_qt(self):
        QApplication.aboutQt()

    def show_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def closeEvent(self, event): #settings will save when closing the app
        self.settings.setValue('window_size', self.size())
        self.settings.setValue('window_pos', self.pos())
        self.settings.setValue('dark_mode', self.actionDarkMode.isChecked())
        event.accept()

    def loadSettings(self): #settings will load when opening the app
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode')
        if size is not None:
            self.resize(size)
        if pos is not None:
            self.move(pos)
        if dark == 'true':
            self.actionDarkMode.setChecked(True)
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())