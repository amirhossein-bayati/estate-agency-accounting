# import sys
# # from PyQt5.uic import loadUi
# # from PyQt5 import QtWidgets
# # from PyQt5.QtWidgets import QDialog, QApplication, QWidget
# # from PyQt5.QtGui import QPixmap

## IMPORTS
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# IMPORT GUI FILE
from main_interface import *


## MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.homeBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.estatesBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.customersBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.contractsBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.employeesBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.InfoBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.aboutUsBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(6))


        self.show()


## EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
