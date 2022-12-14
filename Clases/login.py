import sys
from PyQt5 import QtWidgets, uic #carga intefaz grafica
from PyQt5.uic import loadUi
import mainVistaAdmin
import mainVistaCliente
import bd_loginyRegis
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/pruebaQTd.ui", self) #cambiar
        self.admin=mainVistaAdmin.AdminView()
        self.cliente=mainVistaCliente.ClientView()

        self.setupUiComponents()
        
    def setupUiComponents(self):
        self.pushButton.clicked.connect(self.loginfunction) 


    def loginfunction(self):
        usuario=self.usuarioL.text() #cambiar
        password = self.contraL.text() #cambiar
        print(usuario,password)
        conexion=bd_loginyRegis.conexion_BD("BD/Supermark.db")
        conexion.consulta(usuario,password)
     
       
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    
    form = Login()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()