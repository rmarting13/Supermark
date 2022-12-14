import sys
from PyQt5 import QtWidgets, uic #carga intefaz grafica

from PyQt5.uic import loadUi
import login
import registro

class vistaPrinc(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/principal.ui", self)
        self.login=login.Login()
        self.registro=registro.Register()
        self.setupUiComponents()
    def setupUiComponents(self):
        self.pushButton.clicked.connect(self.login.show)
        self.pushButton_2.clicked.connect(self.registro.show)
        self.toolButton.clicked.connect(self.close)
     
def main():
        app = QtWidgets.QApplication(sys.argv)
        form = vistaPrinc()
        form.show()
        app.exec_()
        

if __name__ == '__main__':
    main()