# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(827, 529)
        icon = QIcon()
        icon.addFile(u":/images/ms_icon.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_about_qt = QAction(MainWindow)
        self.action_about_qt.setObjectName(u"action_about_qt")
        self.action_dark_mode = QAction(MainWindow)
        self.action_dark_mode.setObjectName(u"action_dark_mode")
        self.action_dark_mode.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.line_pokemon_character = QLineEdit(self.tab)
        self.line_pokemon_character.setObjectName(u"line_pokemon_character")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.line_pokemon_character.setFont(font)

        self.horizontalLayout_2.addWidget(self.line_pokemon_character)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.label_name = QLabel(self.groupBox)
        self.label_name.setObjectName(u"label_name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setMinimumSize(QSize(65, 0))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_name.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_name)

        self.label_character = QLabel(self.groupBox)
        self.label_character.setObjectName(u"label_character")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_character.sizePolicy().hasHeightForWidth())
        self.label_character.setSizePolicy(sizePolicy1)
        self.label_character.setMinimumSize(QSize(0, 0))
        self.label_character.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_character)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.label_weight_label = QLabel(self.groupBox)
        self.label_weight_label.setObjectName(u"label_weight_label")
        sizePolicy.setHeightForWidth(self.label_weight_label.sizePolicy().hasHeightForWidth())
        self.label_weight_label.setSizePolicy(sizePolicy)
        self.label_weight_label.setMinimumSize(QSize(65, 0))
        self.label_weight_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_weight_label)

        self.label_weight = QLabel(self.groupBox)
        self.label_weight.setObjectName(u"label_weight")
        sizePolicy1.setHeightForWidth(self.label_weight.sizePolicy().hasHeightForWidth())
        self.label_weight.setSizePolicy(sizePolicy1)
        self.label_weight.setMinimumSize(QSize(0, 0))
        self.label_weight.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_weight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.table1 = QTableWidget(self.groupBox)
        self.table1.setObjectName(u"table1")
        self.table1.setRowCount(0)

        self.horizontalLayout.addWidget(self.table1)

        self.table2 = QTableWidget(self.groupBox)
        self.table2.setObjectName(u"table2")

        self.horizontalLayout.addWidget(self.table2)

        self.table3 = QTableWidget(self.groupBox)
        self.table3.setObjectName(u"table3")

        self.horizontalLayout.addWidget(self.table3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(26)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 827, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.action_about)
        self.menuHelp.addAction(self.action_about_qt)
        self.menuSettings.addAction(self.action_dark_mode)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pokemon REST API Getter", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_about_qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.action_dark_mode.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.line_pokemon_character.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pokemon character (press enter)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Character:", None))
        self.label_character.setText("")
        self.label_weight_label.setText(QCoreApplication.translate("MainWindow", u"Weight:", None))
        self.label_weight.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Stats Getter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Placeholder for something good to come", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

