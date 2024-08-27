# -------------------------------------------------------------------------------
# Name:             Bind.py
# Purpose:          Example of Binding text from a text box to a label real time
# 
# Author:           Jeffreaux
#
# Created:          26Aug24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction,  QLabel, QLineEdit
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("Bind_GUI.ui", self)

        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")
        self.actExit = self.findChild(QAction, "actExit")

        self.txtInput = self.findChild(QLineEdit, "txtInput")
        self.txtInput_2 = self.findChild(QLineEdit, "txtInput_2")
        self.lblOutput = self.findChild(QLabel, "lblOutput")

        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)
        self.actExit.triggered.connect(self.closeEvent)

        # Will trigger at each keypress
        self.txtInput.textChanged.connect(self.changed)  

        # Will trigger when enter is pressed
        self.txtInput_2.editingFinished.connect(self.hit_enter)  

        # Show the app
        self.show()

    
    def changed(self):
        self.lblOutput.setText(self.txtInput.text())
    
    def hit_enter(self):
        self.lblOutput.setText(self.txtInput_2.text())
    
    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
