
import sys
from PyQt5 import QtWidgets, uic #carga intefaz grafica

from PyQt5.uic import loadUi
import vistaAgregProd

class vistaAdmin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/vistaAdmin.ui", self)
        self.agregarP= vistaAgregProd.vistaAgregProd()
        
        self.setupUiComponents()
    def setupUiComponents(self):
      self.pushButton.clicked.connect(self.agregarP.show)
      #boton agregar_producto

    def vistaAdminfunction(self):
       pass

def main():
        app = QtWidgets.QApplication(sys.argv)
        form = vistaAdmin()
        form.show()
        app.exec_()
        

if __name__ == '__main__':
    main()