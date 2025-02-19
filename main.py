import sys
import qdarkstyle
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QSettings, QTimer
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Form as about_ui

class MainWindow(QMainWindow, main_ui): # used to display the main user interface
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = QSettings('settings.ini', QSettings.IniFormat)
        self.settings_manager = SettingsManager(self)  # Initializes SettingsManager
        self.settings_manager.load_settings()  # Load settings when the app starts
        self.pokemon_api = PokemonAPI() # initialize PokemonAPI class

        # Update label_connection based on connection status
        self.update_connection_status()

        # Set up a timer to poll the connection status every 30 seconds
        self.connection_timer = QTimer(self)
        self.connection_timer.timeout.connect(self.update_connection_status)
        self.connection_timer.start(30000)  # 30 seconds in milliseconds

        # button
        self.line_pokemon_character.returnPressed.connect(self.pokemon_get)

        # menubar
        self.action_dark_mode.toggled.connect(self.dark_mode)
        self.action_about.triggered.connect(self.show_about)
        self.action_about_qt.triggered.connect(self.about_qt)

    def update_connection_status(self):
        self.pokemon_api.is_connected = self.pokemon_api.check_connection()
        if self.pokemon_api.is_connected:
            self.label_connection.setText("Connected to PokéAPI")
        else:
            self.label_connection.setText("Failed to connect to PokéAPI")

    def pokemon_get(self):
        # Return all characters if the line is empty
        if not self.line_pokemon_character.text().strip():
            # Clear the table before adding new data
            self.table1.clear()
            self.table2.clear()
            self.table3.clear()
            self.table1.setRowCount(0)
            self.table1.setColumnCount(0)
            self.table2.setRowCount(0)
            self.table2.setColumnCount(0)
            self.table3.setRowCount(0)
            self.table3.setColumnCount(0)

            self.label_character.setText("Fetching all characters...please wait")
            self.label_weight.setText("")
            QApplication.processEvents() # processes all pending events before continuing
            
            all_characters = self.pokemon_api.get_pokemon_data('')
            self.table1.setColumnCount(1)
            self.table1.setHorizontalHeaderLabels(['characters'])
            for row in range(len(all_characters['results'])):
                    name = all_characters['results'][row]['name']
                    self.table1.insertRow(row)
                    self.table1.setItem(row, 0, QTableWidgetItem(name))
                    self.table1.resizeColumnsToContents()
                    self.table1.resizeRowsToContents()
            self.label_character.setText("All Characters")

        # Return a specific character if the line is not empty
        if self.line_pokemon_character.text():  # Only proceed if the API request was successful
            # Clear the table before adding new data
            self.table1.clear()
            self.table2.clear()
            self.table3.clear()
            self.table1.setRowCount(0)
            self.table1.setColumnCount(0)
            self.table2.setRowCount(0)
            self.table2.setColumnCount(0)
            self.table3.setRowCount(0)
            self.table3.setColumnCount(0)

            pokemon_character = self.pokemon_api.get_pokemon_data(self.line_pokemon_character.text())
            name = pokemon_character['name']
            self.label_character.setText(name)
            print(f"Name: {pokemon_character['name']}")
            print(f"Weight: {pokemon_character['weight']}")

            self.table1.setColumnCount(1)
            self.table1.setHorizontalHeaderLabels(['Moves'])
            for row in range(len(pokemon_character['moves'])): # this will return the actual number of moves and stop when there are no more moves
                try:
                    self.table1.insertRow(row)
                    moves = pokemon_character['moves'][row]['move']['name']
                    self.table1.setItem(row, 0, QTableWidgetItem(moves))
                    self.table1.resizeColumnsToContents()
                    self.table1.resizeRowsToContents()
                    print(f"Move {row+1}: {pokemon_character['moves'][row]['move']['name']}")
                except IndexError:
                    break
                except TypeError:
                    break

            self.table2.setColumnCount(1)
            self.table2.setHorizontalHeaderLabels(['Abilities'])
            for row in range(len(pokemon_character['abilities'])):
                try:
                    self.table2.insertRow(row)
                    ability = pokemon_character['abilities'][row]['ability']['name']
                    self.table2.setItem(row, 0, QTableWidgetItem(ability))
                    self.table2.resizeColumnsToContents()
                    self.table2.resizeRowsToContents()
                    print(f"Ability {row+1}: {ability}")
                except IndexError:
                    break
                except TypeError:
                    break
                
            weight = pokemon_character['weight']
            self.label_weight.setText(str(weight))

        print ("thank you")
        
        self.line_pokemon_character.clear()

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def show_about(self): #loads the About window
        self.about_window = AboutWindow(dark_mode=self.action_dark_mode.isChecked())
        self.about_window.show()

    def about_qt(self): #loads the About Qt window
        QApplication.aboutQt()

    def closeEvent(self, event):  # Save settings when closing the app
        self.settings_manager.save_settings()  # Save settings using the manager
        event.accept()

class PokemonAPI: # Connects to the pokeapi website to get the stats
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2/'
        self.is_connected = self.check_connection()

    def check_connection(self):
        try:
            response = requests.get(self.base_url)
            if response.status_code // 100 == 2: # checks for any 2xx status code
                return True
        except requests.RequestException:
            pass
        return False

    def get_pokemon_data(self, pokemon_character):
        url=f'{self.base_url}pokemon/{pokemon_character}/?limit=100000'

        response = requests.get(url)
        if response.status_code // 100 == 2: # checks for any 2xx status code
            return response.json()
        else:
            print(f"Connection failed with status code {response.status_code}")
            return None

class SettingsManager: # used to load and save settings when opening and closing the app
    def __init__(self, main_window):
        self.main_window = main_window
        self.settings = QSettings('settings.ini', QSettings.IniFormat)

    def load_settings(self):
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode')
        
        if size is not None:
            self.main_window.resize(size)
        if pos is not None:
            self.main_window.move(pos)
        if dark == 'true':
            self.main_window.action_dark_mode.setChecked(True)
            self.main_window.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    def save_settings(self):
        self.settings.setValue('window_size', self.main_window.size())
        self.settings.setValue('window_pos', self.main_window.pos())
        self.settings.setValue('dark_mode', self.main_window.action_dark_mode.isChecked())

class AboutWindow(QWidget, about_ui): # Configures the About window
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)

        if dark_mode:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())