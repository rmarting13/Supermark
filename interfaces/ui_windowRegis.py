# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Usuarios\rmarting13\Documentos\Tecnicatura Universitaria en Programación\1000PROGRAMADORES\ProyectoSuperMark\interfaces\windowRegis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt1 = QtWidgets.QLabel(self.centralwidget)
        self.txt1.setGeometry(QtCore.QRect(0, -10, 491, 471))
        self.txt1.setStyleSheet("*{\n"
"background-color:aquamarine;\n"
"}")
        self.txt1.setObjectName("txt1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 80, 111, 51))
        self.label.setStyleSheet("*{\n"
"background-color:beige;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 150, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 240, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 280, 61, 20))
        self.label_4.setObjectName("label_4")
        self.nombreR = QtWidgets.QLineEdit(self.centralwidget)
        self.nombreR.setGeometry(QtCore.QRect(190, 150, 113, 20))
        self.nombreR.setObjectName("nombreR")
        self.emailR = QtWidgets.QLineEdit(self.centralwidget)
        self.emailR.setGeometry(QtCore.QRect(190, 240, 113, 20))
        self.emailR.setObjectName("emailR")
        self.contraR = QtWidgets.QLineEdit(self.centralwidget)
        self.contraR.setGeometry(QtCore.QRect(190, 280, 113, 20))
        self.contraR.setText("")
        self.contraR.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contraR.setObjectName("contraR")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 370, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 180, 61, 20))
        self.label_5.setObjectName("label_5")
        self.direR = QtWidgets.QLineEdit(self.centralwidget)
        self.direR.setGeometry(QtCore.QRect(190, 180, 113, 20))
        self.direR.setObjectName("direR")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 210, 61, 20))
        self.label_6.setObjectName("label_6")
        self.telefR = QtWidgets.QLineEdit(self.centralwidget)
        self.telefR.setGeometry(QtCore.QRect(190, 210, 113, 20))
        self.telefR.setText("")
        self.telefR.setObjectName("telefR")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txt1.setText(_translate("MainWindow", "   SUPERMARK"))
        self.label.setText(_translate("MainWindow", "REGISTRO DE CLIENTE"))
        self.label_2.setText(_translate("MainWindow", "NOMBRE"))
        self.label_3.setText(_translate("MainWindow", "EMAIL"))
        self.label_4.setText(_translate("MainWindow", "PASSWORD"))
        self.pushButton_2.setText(_translate("MainWindow", "REGISTRARSE"))
        self.label_5.setText(_translate("MainWindow", "DIRECCION"))
        self.label_6.setText(_translate("MainWindow", "TELEFONO"))
