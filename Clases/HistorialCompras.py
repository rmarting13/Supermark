import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPropertyAnimation , QEasingCurve , Qt
from HistorialCompras_ui import Ui_MainWindow
from PopUp import Dialogo

class HistorialCompras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupUiComponents()
        self.popUp = Dialogo()

    def setupUiComponents(self):
        self.ui.tablaDetalleCompra.setColumnWidth(0,185)
        self.ui.tablaDetalleCompra.setColumnWidth(1,60)
        self.ui.tablaDetalleCompra.setColumnWidth(2,60)
        self.ui.tablaDetalleCompra.verticalHeader().hide()

        #self.ui.comboBox.activated("").connect(lambda: self.__cargarRegistro("",db))
        self.ui.comboBox.activated.connect(lambda: self.cargarRegistro("",""))

    def cargarHistorial(self,db):
        #para cada registro de compras en la db
        compras = db
        self.ui.comboBox.addItems(compras)

    
    def cargarRegistro(self,orden,db):
        #buscar nro de orden en db
        listaTuplas = db.consula(orden)
        self.ui.lblFecha.setText("aqui va la fecha correspondiente a la compra")
        for row in range(0,db.rowCount()):
            self.ui.tablaDetalleCompra.insertRow(row)
            self.ui.tablaDetalleCompra.setItem(row,0,QtWidgets.QTableWidgetItem(listaTuplas[row][0]))
            self.ui.tablaDetalleCompra.setItem(row,0,QtWidgets.QTableWidgetItem(listaTuplas[row][1]))
            self.ui.tablaDetalleCompra.setItem(row,0,QtWidgets.QTableWidgetItem(listaTuplas[row][2]))
        self.ui.lblCantTotalProd.setText("")
        self.ui.lblSubtotalImporte.setText("")
        self.ui.lblBonifImporte.setText("")
        self.ui.lblTotalImporte.setText("")

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = HistorialCompras()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()