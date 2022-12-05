
import sys
from PyQt5 import QtWidgets, uic #carga intefaz grafica

from PyQt5.uic import loadUi

class vistaCliente(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/vistaCliente.ui", self)
        

    def setupUiComponents(self):
        # self.ingresar.clicked.connect(self.vistaClientefunction)
        pass

    def vistaClientefunction(self):
       pass

def main():
        app = QtWidgets.QApplication(sys.argv)
        
        form = vistaCliente()
        form.show()
        app.exec_()

if __name__ == '__main__':
    main()