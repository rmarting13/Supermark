
import sys
from PyQt5 import QtWidgets, uic #carga intefaz grafica

from PyQt5.uic import loadUi
import producto

class vistaAgregProd(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/vistaAgregProd.ui", self)
        self.setupUiComponents()
    def setupUiComponents(self):
        self.pushButton.clicked.connect(self.traerDatosInterfaz) #cambiar
    def traerDatosInterfaz(self):
      nombre = self.lineEdit.text()
      precio= self.lineEdit_2.text()
      stock= self.lineEdit_3.text()
      print(nombre,precio,stock)
      producto1=producto.Producto(nombre,precio,stock)
      producto1.agregar_producto()
      print("Se agrego correctamente")
   

def main():
      
        app = QtWidgets.QApplication(sys.argv)
        
        form = vistaAgregProd()
        form.show()
        app.exec_()

if __name__ == '__main__':
    main()