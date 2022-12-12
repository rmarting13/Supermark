import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPropertyAnimation , QEasingCurve
from ClientView import Ui_MainWindow
from PopUp import Dialogo

class ClientView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupUiComponents()
        self.popUp = Dialogo()
        self.ui.MenuButton.clicked.connect(self.expandir)

    def expandir(self):
        ancho = self.ui.MenuIzquierdo.width()
        if ancho == 50:
            nuevoAncho = 140
            self.ui.MenuButton.setIcon(QtGui.QIcon("interfaces/icons/arrow-left-44.png"))
        elif ancho == 140:
            nuevoAncho = 50
            self.ui.MenuButton.setIcon(QtGui.QIcon("interfaces/icons/bars.png"))

        try:
            self.animacion = QPropertyAnimation(self.ui.MenuIzquierdo,b"minimumWidth")
            self.animacion.setStartValue(ancho)
            self.animacion.setEndValue(nuevoAncho)
            self.animacion.setDuration(350)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()
        except:
            self.ui.MenuButton.setIcon(QtGui.QIcon("interfaces/ui/icons/bars.png"))
            self.animacion.setStartValue(50)
            self.animacion.setEndValue(50)
            self.animacion.setDuration(350)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()

    def setupUiComponents(self):
        self.ui.btnConfirmar.setDisabled(True)
        self.ui.btnCancelar.setDisabled(True)
        self.ui.btnAgregar.setDisabled(True)
        # self.ingresar.clicked.connect(self.vistaAdminfunction)
        #permite la selección de una fila completa al hacer click en cualquier celda
        self.ui.tablaProductos.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.tablaProductos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tablaSeleccion.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tablaDetalle.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.lblSubtotalImporte.setText(str(0))
        self.ui.lblCantTotalProdSelec.setText(str(0))
        self.ui.tablaProductos.setColumnWidth(0,190)
        self.ui.tablaProductos.setColumnWidth(1,55)
        self.ui.tablaSeleccion.setColumnWidth(0,195)
        self.ui.tablaSeleccion.setColumnWidth(1,60)
        self.ui.tablaSeleccion.setColumnWidth(2,60)
        self.ui.tablaDetalle.setColumnWidth(0,185)
        self.ui.tablaDetalle.setColumnWidth(1,60)
        self.ui.tablaDetalle.setColumnWidth(2,60)
        self.ui.tablaDetalle.verticalHeader().hide()
        self.ui.tablaProductos.verticalHeader().hide()
        self.ui.tablaSeleccion.verticalHeader().hide()

        self.__cargarDatosCuenta()
        self.__cargarProductosDB()
        
        self.ui.tablaProductos.clicked.connect(self.__funcionAlClickearCeldasTablaProductos)
        
        self.ui.InicioButton.clicked.connect(self.__accionBtnInicio)
        self.ui.CuentaButton.clicked.connect(self.__accionBtnCuenta)
        self.ui.CompraButton.clicked.connect(self.__accionBtnCompra)
        self.ui.btnCerrarSesion.clicked.connect(self.__accionBtnCerrarSesion)
        self.ui.btnAgregar.clicked.connect(self.__accionBtnAgregarAlCarrito)
        self.ui.btnCancelar.clicked.connect(self.__accionBtnCancelarCompra)
        self.ui.btnConfirmar.clicked.connect(self.__accionBtnConfirmarCompra)
    
    def __accionBtnInicio(self):
        self.ui.Paginas.setCurrentWidget(self.ui.PaginaInicio)
        color = self.ui.InicioButton.styleSheet()
        self.ui.InicioButton.setStyleSheet(color.replace("transparent","#ffdd52"))
        self.ui.CuentaButton.setStyleSheet(self.ui.CuentaButton.styleSheet().replace("#1aa7ff","transparent"))
        self.ui.CompraButton.setStyleSheet(self.ui.CompraButton.styleSheet().replace("#8ebf19","transparent"))
    
    def __accionBtnCuenta(self):
        self.ui.Paginas.setCurrentWidget(self.ui.PaginaCuenta)
        color = self.ui.CuentaButton.styleSheet()
        self.ui.CuentaButton.setStyleSheet(color.replace("transparent","#1aa7ff"))
        self.ui.InicioButton.setStyleSheet(self.ui.InicioButton.styleSheet().replace("#ffdd52","transparent"))
        self.ui.CompraButton.setStyleSheet(self.ui.CompraButton.styleSheet().replace("#8ebf19","transparent"))
        
    def __accionBtnCompra(self):
        self.ui.Paginas.setCurrentWidget(self.ui.PaginaComprar)
        color = self.ui.CompraButton.styleSheet()
        self.ui.CompraButton.setStyleSheet(color.replace("transparent","#8ebf19"))
        self.ui.InicioButton.setStyleSheet(self.ui.InicioButton.styleSheet().replace("#ffdd52","transparent"))
        self.ui.CuentaButton.setStyleSheet(self.ui.CuentaButton.styleSheet().replace("#1aa7ff","transparent"))

    def __accionBtnCerrarSesion(self):
        #llamar al método que inicia la ui de registro
        self.close()

    def __cargarDatosCuenta(self):
        self.ui.lblUsuario_2.setText("Cosme Fulanito")
        self.ui.lblEmail_2.setText("cosmefulanito@example.com")
        self.ui.lblDom_2.setText("Av. Siempre Viva 742, Springfield")
        self.ui.lblBonif_2.setText("Si")

    
    def __cargarProductosDB(self):
        row = self.ui.tablaProductos.rowCount()
        self.ui.tablaProductos.insertRow(row)
        self.ui.tablaProductos.setItem(row, 0, QtWidgets.QTableWidgetItem("Papas"))
        self.ui.tablaProductos.setItem(row, 1, QtWidgets.QTableWidgetItem("250"))

        row = self.ui.tablaProductos.rowCount()
        self.ui.tablaProductos.insertRow(row)
        self.ui.tablaProductos.setItem(row, 0, QtWidgets.QTableWidgetItem("Merca"))
        self.ui.tablaProductos.setItem(row, 1, QtWidgets.QTableWidgetItem("760"))

    def __funcionAlClickearCeldasTablaProductos(self):
        if int(self.ui.lblCantTotalProdSelec.text()) < 30:
            desc = self.ui.tablaProductos.selectedIndexes()[0].data()
             #evita que se seleccione un producto ya agregado
            if not self.__productoAgregado(desc):
                precio = self.ui.tablaProductos.selectedIndexes()[1].data()
                row = self.ui.tablaSeleccion.rowCount()
                self.ui.tablaSeleccion.insertRow(row)
                self.ui.tablaSeleccion.setItem(row,0,QtWidgets.QTableWidgetItem(desc))
                #agrega una columna con QSpinBox
                self.ui.tablaSeleccion.setCellWidget(row,1,QtWidgets.QSpinBox(minimum=0,maximum=30))
                self.ui.tablaSeleccion.setItem(row,2,QtWidgets.QTableWidgetItem(str(0)))       
                self.ui.tablaSeleccion.cellWidget(row,1).valueChanged.connect(lambda: self.__funcionSpinBox(precio,row))
        else:
             self.popUp.abrirDialogo("No se pueden seleccionar más productos!")

    def __productoAgregado(self,prod):
        if self.ui.tablaSeleccion.rowCount()!=0:
            productos=[]
            for i in range(self.ui.tablaSeleccion.rowCount()):
                productos.append(self.ui.tablaSeleccion.item(i,0).text())
            value = prod in productos
        else:
            value = False
        return value

    def __funcionSpinBox(self,precio,row):
        if int(self.ui.lblCantTotalProdSelec.text()) < 30:
            sub = int(precio)*self.ui.tablaSeleccion.cellWidget(row,1).value()
            self.ui.tablaSeleccion.setItem(row,2,QtWidgets.QTableWidgetItem(str(sub)))
            suma = 0; cant = 0
            for i in range(row+1):
                cant = cant + self.ui.tablaSeleccion.cellWidget(i,1).value()
                suma = suma + float(self.ui.tablaSeleccion.item(i,2).text())
            self.ui.lblCantTotalProdSelec.setText(str(cant))
            self.ui.lblSubtotalSelec.setText(str(suma))
            if int(self.ui.lblCantTotalProdSelec.text())!=0:
                self.ui.btnAgregar.setDisabled(False)
            else:
                self.ui.btnAgregar.setDisabled(True)
        else:
             self.popUp.abrirDialogo("No se pueden seleccionar más productos!")

    def __accionBtnAgregarAlCarrito(self):
        if self.ui.tablaSeleccion.rowCount()!=0:
            suma = 0; bonif = 0
            for row in range(0,self.ui.tablaSeleccion.rowCount()):
                if self.ui.tablaSeleccion.item(row,2).text() != "0":
                    desc = self.ui.tablaSeleccion.item(row,0).clone()
                    cant = self.ui.tablaSeleccion.cellWidget(row,1).value()
                    sub = self.ui.tablaSeleccion.item(row,2).clone()
                    rowDet = self.ui.tablaDetalle.rowCount()
                    self.ui.tablaDetalle.insertRow(rowDet)
                    self.ui.tablaDetalle.setItem(rowDet, 0, desc)
                    self.ui.tablaDetalle.setItem(rowDet, 1, QtWidgets.QTableWidgetItem(str(cant)))
                    self.ui.tablaDetalle.setItem(rowDet, 2, sub)
                    suma = suma+float(sub.text())
            actual = float(self.ui.lblSubtotalImporte.text())
            self.ui.lblSubtotalImporte.setText(f"{actual+suma}")
            if self.ui.lblBonif_2.text().upper() == "SI":
                bonif = float(self.ui.lblSubtotalImporte.text())*0.10
            self.ui.lblBonifImporte.setText(str(bonif))
            self.ui.lblTotalImporte.setText(str((actual+suma)-bonif))
            #Se limpia la lista de productos seleccionados para evitar agregar productos repetidos en el carrito
            self.popUp.abrirDialogo("Productos agregados con éxito!")
            self.__eliminarFilas(self.ui.tablaSeleccion)
            self.ui.lblCantTotalProdSelec.setText("0")
            self.ui.lblSubtotalSelec.setText("0")
            self.ui.btnAgregar.setDisabled(True)
            self.ui.btnConfirmar.setDisabled(False)
            self.ui.btnCancelar.setDisabled(False)
    
    def __accionBtnCancelarCompra(self):
        self.popUp.abrirDialogo("Se ha cancelado la compra!")
        self.__eliminarFilas(self.ui.tablaDetalle)
        self.ui.lblSubtotalImporte.setText("0")
        self.ui.lblBonifImporte.clear()
        self.ui.lblTotalImporte.clear()
        self.ui.btnCancelar.setDisabled(True)
        self.ui.btnConfirmar.setDisabled(True)
        
    def __eliminarFilas(self,tabla=QtWidgets.QTableWidget):
        cant = tabla.rowCount()
        for row in range(0,cant+1):
            tabla.removeRow(row)

    def __accionBtnConfirmarCompra(self):
        self.popUp.abrirDialogo("Se ha confirmado la compra!")
        self.ui.btnConfirmar.setDisabled(True)
        

   

    def vistaAdminfunction(self):
       pass

def main():
        app = QtWidgets.QApplication(sys.argv)
        form = ClientView()
        form.show()
        app.exec_()

if __name__ == '__main__':
    main()