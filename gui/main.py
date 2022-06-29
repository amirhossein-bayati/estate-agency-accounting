## IMPORTS
import os
import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

# IMPORT GUI FILE
from main_interface import *
# from dialog import *

# IMPORT DB
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))
import models, queries
from models import *


## MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # dialog = QDialog()
        # dialog.ui = Ui_dialog()
        # dialog.ui.setupUi(dialog)
        
        self.switchPages()
        self.setTableHeaders()
        
        self.show()
        # if(not self.ui.user):
        #     sys.exit()
        # else:
        #     self.show()


    def switchPages(self):
        self.ui.homeBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.estatesBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.customersBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.contractsBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.employeesBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.InfoBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.aboutUsBtn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(6))

    def setTableHeaders(self):
        attr = vars(models.Estate).keys()
        attr = [a for a in attr if not(a.startswith("__") or a.startswith("_"))]
        attr = [x.replace("_", " ") for x in attr]
        self.ui.tableWidget_2.setHorizontalHeaderLabels(attr)
        attr = vars(models.Customer).keys()
        attr = [a for a in attr if not(a.startswith("__") or a.startswith("_"))]
        attr = [x.replace("_", " ") for x in attr]
        self.ui.tableWidget_3.setHorizontalHeaderLabels(attr)
        attr = vars(models.Contract).keys()
        attr = [a for a in attr if not(a.startswith("__") or a.startswith("_"))]
        attr = [x.replace("_", " ") for x in attr]
        self.ui.tableWidget_4.setHorizontalHeaderLabels(attr)
        attr = vars(models.Employee).keys()
        attr = [a for a in attr if not(a.startswith("__") or a.startswith("_") or a.startswith("username") or a.startswith("password"))]
        attr = [x.replace("_", " ") for x in attr]
        self.ui.tableWidget_5.setHorizontalHeaderLabels(attr)


## EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
