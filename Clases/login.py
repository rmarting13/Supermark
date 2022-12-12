import sys
from PyQt5 import QtWidgets, QtSql, uic #carga intefaz grafica
from PyQt5.uic import loadUi
import vistaAdmin
import vistaCliente
import registro

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/pruebaQTd.ui", self) #cambiar
        self.admin=vistaAdmin.vistaAdmin()
        self.cliente=vistaCliente.vistaCliente()
        self.registro=registro.Register()

        self.openDB()
        self.setupUiComponents()

    def setupUiComponents(self):
        self.pushButton.clicked.connect(self.loginfunction) #cambiar
        self.pushButton_2.clicked.connect(self.registro.show) #cambiar
           
    def openDB(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("BD/Supermark.db")# Cambiar poner el nombre de su base de datos
        if not self.db.open():
            print("error")
        self.query = QtSql.QSqlQuery()
        print('fin')

    def loginfunction(self):
        usuario=self.usuarioL.text() #cambiar
        password = self.contraL.text() #cambiar
        print( password,usuario)

        self.query.exec_("SELECT * FROM Usuarios as U INNER JOIN Rol as R ON U.idrol=R.id_rol where email = '%s' and password='%s';"%(usuario, password))
        self.query.first()
        if self.query.value("email") != None and self.query.value("password")!= None:
            print("se ingreso exitosamente")
            if self.query.value('nombre')=='admin':
                 self.admin.show()
            else:
                 self.cliente.show()

        else:
            print("error al ingresar")
             #self.usuario.clear()
             #self.password.clear()
       
        

        
def main():
    app = QtWidgets.QApplication(sys.argv)
    
    form = Login()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()