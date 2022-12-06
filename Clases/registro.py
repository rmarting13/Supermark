import sys
from PyQt5 import QtWidgets, QtSql, uic #carga intefaz grafica
from PyQt5.uic import loadUi
# import vistaAdmin


class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/windowRegis.ui", self) #cambiar
        #self.admin=vistaAdmin.vistaAdmin()
       
        self.openDB()
        self.setupUiComponents()

    def setupUiComponents(self):
        self.pushButton_2.clicked.connect(self.registerfunction) #cambiar

    def openDB(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("BD/Supermark.db")# Cambiar poner el nombre de su base de datos
        if not self.db.open():
            print("error")
        self.query = QtSql.QSqlQuery()
        print('fin')

    def registerfunction(self):
        nombre=self.nombreR.text() #cambiar
        email=self.emailR.text()
        password = self.contraR.text() #cambiar

        print(nombre,email,password)
        self.query.exec_(f'INSERT INTO Usuarios VALUES (NULL,"{email}","{password}","{nombre}",2)')
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Register()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()