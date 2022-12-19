import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPropertyAnimation , QEasingCurve , Qt
from HistorialCompras_ui import Ui_MainWindow
from PopUp import Dialogo
import bd_ventas_produc

class HistorialCompras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupUiComponents()
        self.popUp = Dialogo()

    def setupUiComponents(self):
        self.ui.tablaDetalleCompra.setColumnWidth(0,200)
        self.ui.tablaDetalleCompra.setColumnWidth(1,60)
        self.ui.tablaDetalleCompra.setColumnWidth(2,90)
        self.ui.tablaDetalleCompra.verticalHeader().hide()
        self.ui.comboBox.currentTextChanged.connect(lambda: self.__cargarRegistro())

    def cargarHistorial(self,idUsuario):
        #para cada registro de compras en la db
        nroCompras = bd_ventas_produc.extrerNumerosDeCompras(idUsuario)
        for item in nroCompras:
            if self.ui.comboBox.findText(str(item[0]),Qt.MatchExactly) == -1:
                self.ui.comboBox.addItem(str(item[0]),str(item[0]))
    
    def limpiarHistorial(self):
        self.ui.comboBox.clear()

    def __cargarRegistro(self):
        self.__limpiarFormulario()
        orden = self.ui.comboBox.currentText()
        print("orden: "+orden)
        #buscar nro de orden en db
        tupla = bd_ventas_produc.extraer_compra(orden)
        prod = self.__formatearStringATupla(tupla[3])
        cant = self.__formatearStringATupla(tupla[4])
        sub = self.__formatearStringATupla(tupla[5])
        print(prod)

        self.ui.lblFecha.setText(tupla[2])
        if len(prod)>1:
            ind = 1
        else:
            ind = 0
        for row in range(len(prod)-ind):
            self.ui.tablaDetalleCompra.insertRow(row)
            self.ui.tablaDetalleCompra.setItem(row,0,QtWidgets.QTableWidgetItem(prod[row]))
            self.ui.tablaDetalleCompra.setItem(row,1,QtWidgets.QTableWidgetItem(cant[row]))
            self.ui.tablaDetalleCompra.setItem(row,2,QtWidgets.QTableWidgetItem(sub[row]))
        self.ui.lblCantTotalProd.setText(str(tupla[6]))
        self.ui.lblSubtotalImporte.setText(str(tupla[7]))
        self.ui.lblBonifImporte.setText(str(tupla[8]))
        self.ui.lblTotalImporte.setText(str(tupla[9]))
        
    def __formatearStringATupla(self,cad):
        tupla = cad.replace("[","")
        tupla = tupla.replace("]","")
        tupla = tupla.replace("'","")
        lista = tupla.split(",")
        return lista

    def __eliminarFilas(self,tabla=QtWidgets.QTableWidget):
        cant = tabla.rowCount()
        for row in range(cant,-1,-1):
            tabla.removeRow(row)

    def __limpiarFormulario(self):
        self.__eliminarFilas(self.ui.tablaDetalleCompra)
        self.ui.lblSubtotalImporte.setText("0")
        self.ui.lblCantTotalProd.setText("0")
        self.ui.lblBonifImporte.setText("0")
        self.ui.lblTotalImporte.setText("0")


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = HistorialCompras()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()