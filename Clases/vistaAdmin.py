
import sys
from PyQt5 import QtWidgets, uic #carga intefaz grafica

from PyQt5.uic import loadUi

class vistaAdmin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/vistaAdmin.ui", self)
        

    def setupUiComponents(self):
        # self.ingresar.clicked.connect(self.vistaAdminfunction)
        pass

    def vistaAdminfunction(self):
       pass

def main():
        app = QtWidgets.QApplication(sys.argv)
        
        form = vistaAdmin()
        form.show()
        app.exec_()

if __name__ == '__main__':
    main()