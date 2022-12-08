
import sys
from PyQt5 import QtWidgets, uic #carga intefaz grafica

from PyQt5.uic import loadUi
import vistaAgregProd
import vistaVerProd
class vistaAdmin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/vistaAdmin.ui", self)
        self.agregarP= vistaAgregProd.vistaAgregProd()
        self.verP=vistaVerProd.vistaVerProd()
        self.setupUiComponents()

    def setupUiComponents(self):
      self.pushButton.clicked.connect(self.agregarP.show)
      #boton agregar_producto
      self.botonVer.clicked.connect(self.verP.show)
      #boton ver_productos

    def vistaAdminfunction(self):
       pass

def main():
        app = QtWidgets.QApplication(sys.argv)
        form = vistaAdmin()
        form.show()
        app.exec_()
        

if __name__ == '__main__':
    main()