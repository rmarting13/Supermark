import sys
from PyQt5 import QtWidgets,uic #carga intefaz grafica

from PyQt5.uic import loadUi
import producto
class vistaVerProd(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/vistaVerProd.ui", self)
        self.setupUiComponents()
    def setupUiComponents(self):
        self.pushButton.clicked.connect(self.ver_productos)
        #self.pushButton.clicked.connect(self.crear_tabla)
        self.pushButton_2.clicked.connect(self.close)
    def ver_productos(self):
       datos=producto.Producto.ver_productos()
       print(datos)
       row = 0
       for endian in datos:
        self.tableWidget.setRowCount(row + 1)
        self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(endian[0])))
        self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(endian[1])))
        self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(endian[2])))
        self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(endian[3])))
        row +=1
    def actualizar_producto(self):
       pass
       #ver_productos()
    #def crear_tabla(self):
     #   tTabla=producto.Producto.tamanioTabla()
      #  self.tableWidget.setRowCount(tTabla)
def main():
        app = QtWidgets.QApplication(sys.argv)
        form = vistaVerProd()
        form.show()
        app.exec_()

if __name__ == '__main__':
    main()
    