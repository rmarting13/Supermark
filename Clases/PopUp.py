# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPropertyAnimation , QEasingCurve
from ClientView import Ui_MainWindow
from PopUp_ui import Ui_Dialog

class Dialogo(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.close())

    def abrirDialogo(self,msj):
        self.ui.label.setText(msj)
        self.exec()