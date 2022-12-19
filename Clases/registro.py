import sys
from PyQt5 import QtWidgets, QtSql, uic #carga intefaz grafica
from PyQt5.uic import loadUi
import vistaDialog
import bd_loginyRegis
class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/windowRegis.ui", self) 
        self.vistaDialog =vistaDialog.vistaDialog()
        self.setupUiComponents()
        
    
    def setupUiComponents(self):
        self.pushButton_2.clicked.connect(self.registerfunction) #cambiar
        self.pushButton_2.clicked.connect(self.vistaDialog.show)
        self.pushButton_2.clicked.connect(self.close)


    def registerfunction(self):
         nombre=self.nombreR.text() 
         direccion = self.direR.text()
         telefono = self.telefR.text()
         email=self.emailR.text()
         password = self.contraR.text()
         conexion=bd_loginyRegis.conexion_BD("BD/Supermark.db")
         conexion.consulta2(nombre,direccion,telefono,email,password)
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Register()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()