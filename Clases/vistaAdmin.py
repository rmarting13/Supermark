
import sys
from PyQt5 import QtWidgets, uic #carga intefaz grafica

from PyQt5.uic import loadUi
import producto
import vistaAgregProd
import vistaVerProd
import vistaBuscarProd
import vistaEliminarProd
class vistaAdmin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/vistaAdmin.ui", self)
        self.agregarP= vistaAgregProd.vistaAgregProd()
        self.verP=vistaVerProd.vistaVerProd()
        self.buscarP=vistaBuscarProd.vistaBuscarProd()
        self.eliminP=vistaEliminarProd.vistaEliminarProd()
        self.setupUiComponents()

    def setupUiComponents(self):
      self.pushButton.clicked.connect(self.agregarP.show)
      #boton agregar_producto
      self.botonVer.clicked.connect(self.verP.show)
      #boton ver_productos
      self.botonBP.clicked.connect(self.buscarP.show)
      #boton buscarP
      self.botonElim.clicked.connect(self.eliminP.show)
      #boton eliminar
      self.pushButton_2.clicked.connect(self.cerrarSession)
      self.pushButton_2.clicked.connect(self.close)

    def cerrarSession(self):
       producto.Producto.cerrarBd()

def main():
        app = QtWidgets.QApplication(sys.argv)
        form = vistaAdmin()
        form.show()
        app.exec_()
        

if __name__ == '__main__':
    main()