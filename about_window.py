from PySide6.QtWidgets import QMainWindow
from about_ui import Ui_MainWindow as about_ui
import qdarkstyle

class AboutWindow(QMainWindow, about_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #darkstyle
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
