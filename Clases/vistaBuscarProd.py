import sys
from PyQt5 import QtWidgets, uic #carga intefaz grafica

from PyQt5.uic import loadUi
import producto

class vistaBuscarProd(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaces/vistaBuscarProd.ui", self)
        
        self.setupUiComponents()

    def setupUiComponents(self):
       self.pushButton.clicked.connect(self.ver_productos)
       self.pushButton_2.clicked.connect(self.buscarProducto)
       self.pushButton_3.clicked.connect(self.actualizar_producto)
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
    def buscarProducto(self):
        id_buscar=self.spinBox.value()
        tTabla=producto.Producto.tamanioTabla()
        if id_buscar<tTabla:
            tabla=producto.Producto.verSoloUnProducto(id_buscar)
            #QtWidgets.QLineEdit.text=str(tabla[0][2])
            #self.lineEdit_2.setText(str(tabla[0][2]))
            #self.lineEdit_3.setText(str(tabla[0][3]))        
            #muestra de datos 
        else:
             print("agrega un id")
        return id_buscar
    def actualizar_producto(self):
        id_buscar = self.buscarProducto()
        nombre = self.lineEdit.text()
        precio= self.lineEdit_2.text()
        stock= self.lineEdit_3.text()
        print(id_buscar,nombre,precio,stock)
        producto1=producto.Producto(nombre,precio,stock,id_buscar)
        print(producto1)
        producto1.actualizar_producto()
        print("Se actualizo correctamente")
def main():
        app = QtWidgets.QApplication(sys.argv)
        form = vistaBuscarProd()
        form.show()
        app.exec_()
        

if __name__ == '__main__':
    main()