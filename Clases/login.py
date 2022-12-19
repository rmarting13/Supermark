import sys
from PyQt5 import QtWidgets, uic #carga intefaz grafica
from PyQt5.uic import loadUi
import mainVistaAdmin
import mainVistaCliente
import bd_loginyRegis
from PopUp import Dialogo
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/pruebaQTd.ui", self) #cambiar
        self.admin=mainVistaAdmin.AdminView()
        self.cliente=mainVistaCliente.ClientView()
        self.popUp = Dialogo()
        self.setupUiComponents()
        
    def setupUiComponents(self):
        self.pushButton.clicked.connect(self.loginfunction)
           


    def loginfunction(self):
        usuario=self.usuarioL.text() #cambiar
        password = self.contraL.text() #cambiar
        conexion=bd_loginyRegis.conexion_BD("BD/Supermark.db")
        op=conexion.consulta(usuario,password)
        id=conexion.consulta3(usuario,password)
        if op==1:
                 print("acceso admin")
                 self.admin.datos(id)
                 self.admin.show()
                 self.close()
               
        elif op==2:
                print("acceso cliente")
                self.cliente.datos(id)
                self.cliente.show()
                self.close()
               
        else:
            self.popUp.abrirDialogo("clave o usuario incorrecto \nIngrese nuevamente")
            
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    
    form = Login()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()