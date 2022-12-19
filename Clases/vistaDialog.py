import sys
from PyQt5 import QtWidgets, uic #carga intefaz grafica

from PyQt5.uic import loadUi

class vistaDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/vistaDialog.ui", self)
        self.setupUiComponents()


    def setupUiComponents(self):
      self.buttonBox.clicked.connect(self.close)

def main():
        app = QtWidgets.QApplication(sys.argv)
        form = vistaDialog()
        form.show()
        app.exec_()
        

if __name__ == '__main__':
    main()