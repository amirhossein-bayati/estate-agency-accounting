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

# IMPORT DB
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))
import models

from models import *
# from models import Customer


## MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.switchPages()
        self.setTableHeaders()
        self.loadData()

        self.show()

    def switchPages(self):
        self.ui.homeBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.estatesBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.customersBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.contractsBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.employeesBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.InfoBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.aboutUsBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(6))

    def setTableHeaders(self):
        self.ui.tableWidget_3.setHorizontalHeaderLabels(["id", "first_name", "last_name", "identity_card", "mobile", "email", "address"])

    def loadData(self):
        customer = models.Customer.query.all()
        print(customer[0].mobile)

        tableRow = 0
        # for row in range(len(customer)):
        #     self.ui.tableWidget_3.setItem(tableRow, 0, customer[0])
        #     tableRow+=1

## EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
