
import sys
from PyQt5 import QtWidgets, QtGui #carga intefaz grafica
from PyQt5.QtCore import QPropertyAnimation , QEasingCurve
from AdminView import Ui_MainWindow
from PopUp import Dialogo

class AdminView(QtWidgets.QMainWindow):
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
            self.ui.MenuButton.setIcon(QtGui.QIcon("interfaces/icons/bars.png"))
            self.animacion.setStartValue(50)
            self.animacion.setEndValue(50)
            self.animacion.setDuration(350)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()

    def setupUiComponents(self):
        self.ui.btnAgregar.setDisabled(True)
        self.ui.btnEliminar.setDisabled(True)
        self.ui.btnModificar.setDisabled(True)
        # self.ingresar.clicked.connect(self.vistaAdminfunction)
        #permite la selección de una fila completa al hacer click en cualquier celda
        self.ui.tablaProductos.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.tablaProductos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tablaClientes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ui.tablaClientes.setColumnWidth(0,190)
        self.ui.tablaClientes.setColumnWidth(1,190)
        self.ui.tablaClientes.setColumnWidth(2,80)
        self.ui.tablaClientes.setColumnWidth(3,80)
        self.ui.tablaProductos.setColumnWidth(0,230)
        self.ui.tablaProductos.setColumnWidth(1,60)
        self.ui.tablaProductos.setColumnWidth(2,80)
        self.ui.tablaDetalleCompra.setColumnWidth(0,210)
        self.ui.tablaDetalleCompra.setColumnWidth(1,60)
        self.ui.tablaDetalleCompra.setColumnWidth(2,80)

        self.__cargarDatosCuenta()
        self.__cargarProductosDB()
        self.__controlEntradaDeTexto()

        self.ui.tablaProductos.cellClicked.connect(self.__funcionAlClickearCeldasTablaProductos)
        self.ui.tablaClientes.cellClicked.connect(self.__funcionAlClickearCeldasTablaClientes)

        self.ui.InicioButton.clicked.connect(self.__accionBtnInicio)
        self.ui.CuentaButton.clicked.connect(self.__accionBtnCuenta)
        self.ui.InventarioButton.clicked.connect(self.__accionBtnInventario)
        self.ui.btnCerrarSesion.clicked.connect(self.__accionBtnCerrarSesion)
        self.ui.btnAgregar.clicked.connect(self.__accionBtnAgregar)
        self.ui.btnEliminar.clicked.connect(self.__accionBtnEliminar)
        self.ui.btnModificar.clicked.connect(self.__accionBtnModificar)
        
    def __accionBtnInicio(self):
        self.ui.Paginas.setCurrentWidget(self.ui.PaginaInicio)
        color = self.ui.InicioButton.styleSheet()
        self.ui.InicioButton.setStyleSheet(color.replace("transparent","#ffdd52"))
        self.ui.CuentaButton.setStyleSheet(self.ui.CuentaButton.styleSheet().replace("#1aa7ff","transparent"))
        self.ui.InventarioButton.setStyleSheet(self.ui.InventarioButton.styleSheet().replace("#8ebf19","transparent"))
    
    def __accionBtnCuenta(self):
        self.ui.Paginas.setCurrentWidget(self.ui.PaginaCuenta)
        color = self.ui.CuentaButton.styleSheet()
        self.ui.CuentaButton.setStyleSheet(color.replace("transparent","#1aa7ff"))
        self.ui.InicioButton.setStyleSheet(self.ui.InicioButton.styleSheet().replace("#ffdd52","transparent"))
        self.ui.InventarioButton.setStyleSheet(self.ui.InventarioButton.styleSheet().replace("#8ebf19","transparent"))
        
    def __accionBtnInventario(self):
        self.ui.Paginas.setCurrentWidget(self.ui.PaginaInventario)
        color = self.ui.InventarioButton.styleSheet()
        self.ui.InventarioButton.setStyleSheet(color.replace("transparent","#8ebf19"))
        self.ui.InicioButton.setStyleSheet(self.ui.InicioButton.styleSheet().replace("#ffdd52","transparent"))
        self.ui.CuentaButton.setStyleSheet(self.ui.CuentaButton.styleSheet().replace("#1aa7ff","transparent"))

    def __accionBtnCerrarSesion(self):
        #llamar al método que inicia la ui de registro
        self.close()

    def __cargarDatosCuenta(self):
        #Conectar con la DB
        self.ui.lblUsuario_2.setText("Cosme Fulanito")
        self.ui.lblEmail_2.setText("cosmefulanito@example.com")
        self.ui.lblDom_2.setText("Av. Siempre Viva 742, Springfield")

    def __cargarProductosDB(self):
        row = self.ui.tablaProductos.rowCount()
        self.ui.tablaProductos.insertRow(row)
        self.ui.tablaProductos.setItem(row, 0, QtWidgets.QTableWidgetItem("Papas"))
        self.ui.tablaProductos.setItem(row,1,QtWidgets.QTableWidgetItem("50"))
        self.ui.tablaProductos.setItem(row, 1, QtWidgets.QTableWidgetItem("250"))
    
    def __controlEntradaDeTexto(self):
        self.ui.lineEditDescripcion.textChanged.connect(self.__enableDisableBtnAgregar)
        self.ui.lineEditCantidad.textChanged.connect(self.__enableDisableBtnAgregar)
        self.ui.lineEditPrecio.textChanged.connect(self.__enableDisableBtnAgregar)
        self.ui.lineEditDescripcion_2.textChanged.connect(self.__enableDisableBtnModificarEliminar)
        self.ui.lineEditCantidad_2.textChanged.connect(self.__enableDisableBtnModificarEliminar)
        self.ui.lineEditPrecio_2.textChanged.connect(self.__enableDisableBtnModificarEliminar)

    def __enableDisableBtnAgregar(self):
        if self.ui.lineEditDescripcion.text()!="" and self.ui.lineEditCantidad.text()!="" and self.ui.lineEditPrecio.text()!="":
            self.ui.btnAgregar.setDisabled(False)
        else:
            self.ui.btnAgregar.setDisabled(True)


    def __enableDisableBtnModificarEliminar(self):
        if self.ui.lineEditDescripcion_2.text()!="" and self.ui.lineEditCantidad_2.text()!="" and self.ui.lineEditPrecio_2.text()!="":
            self.ui.btnModificar.setDisabled(False)
            self.ui.btnEliminar.setDisabled(False)
        else:
            self.ui.btnModificar.setDisabled(True)
            self.ui.btnEliminar.setDisabled(True)

    def __accionBtnAgregar(self):
        desc = self.ui.lineEditDescripcion.text()
        cant = self.ui.lineEditCantidad.text()
        precio = self.ui.lineEditPrecio.text()
        row = self.ui.tablaProductos.rowCount()
        self.ui.tablaProductos.insertRow(row)
        
        self.ui.tablaProductos.setItem(row, 0, QtWidgets.QTableWidgetItem(desc))
        self.ui.tablaProductos.setItem(row, 1, QtWidgets.QTableWidgetItem(cant))
        self.ui.tablaProductos.setItem(row, 2, QtWidgets.QTableWidgetItem(precio))
        
        self.popUp.abrirDialogo("Producto agregado con éxito!")
        #Se limpian los campos
        self.ui.lineEditDescripcion.clear()
        self.ui.lineEditCantidad.clear()
        self.ui.lineEditPrecio.clear()
        self.ui.btnAgregar.setDisabled(True)
  
    def __accionBtnModificar(self):
        selectedRow = self.ui.tablaProductos.selectionModel().selectedRows()[0]
        desc = self.ui.lineEditDescripcion_2.text()
        cant = self.ui.lineEditCantidad_2.text()
        precio = self.ui.lineEditPrecio_2.text()
        self.ui.tablaProductos.setItem(selectedRow.row(),0,QtWidgets.QTableWidgetItem(desc))
        self.ui.tablaProductos.setItem(selectedRow.row(),1,QtWidgets.QTableWidgetItem(cant))
        self.ui.tablaProductos.setItem(selectedRow.row(),2,QtWidgets.QTableWidgetItem(precio))
        self.popUp.abrirDialogo("Producto modificado con éxito!")
        self.ui.lineEditDescripcion_2.clear()
        self.ui.lineEditCantidad_2.clear()
        self.ui.lineEditPrecio_2.clear()
        self.ui.btnModificar.setDisabled(True)
    
    def __accionBtnEliminar(self):
        selectedRows = self.ui.tablaProductos.selectionModel().selectedRows()
        for row in selectedRows:
            self.ui.tablaProductos.removeRow(row.row())
        self.popUp.abrirDialogo("Producto eliminado con éxito!")
        self.ui.lineEditDescripcion_2.clear()
        self.ui.lineEditCantidad_2.clear()
        self.ui.lineEditPrecio_2.clear()
        self.ui.btnEliminar.setDisabled(True)

    def __funcionAlClickearCeldasTablaProductos(self):
        desc = self.ui.tablaProductos.selectedIndexes()[0].data()
        cant = self.ui.tablaProductos.selectedIndexes()[1].data()
        precio = self.ui.tablaProductos.selectedIndexes()[2].data()

        self.ui.lineEditDescripcion_2.setText(str(desc))
        self.ui.lineEditCantidad_2.setText(str(cant))
        self.ui.lineEditPrecio_2.setText(str(precio))
        self.ui.btnEliminar.setDisabled(False)
        self.ui.btnModificar.setDisabled(False)

    
    def __funcionAlClickearCeldasTablaClientes(self):
        #Conectar con la base de datos
        nombre = self.ui.tablaProductos.selectedIndexes()[0].data()
        #self._cargarDetalleDeCompra(nombre,bd)
        self.ui.lblNroCompra_2.setText(self.ui.tablaProductos.selectedIndexes()[4].data())


    def __cargarDetalleDeCompra(self,nombre,db):
        #buscar nombre en db
        # row es la lista de datos de la tabla compra de un cliente de la base de datos (db)
        #lista = guardar la tabla del detalle de compra del cliente
        # for row in lista:
        #     rowDet = self.ui.tablaDetalle.rowCount()
        #     self.ui.tablaDetalleCompra.insertRow(rowDet)
        #     self.ui.tablaDetalleCompra.setItem(rowDet, 0, QtWidgets.QTableWidgetItem(str(row[0])))
        #     self.ui.tablaDetalleCompra.setItem(rowDet, 1, QtWidgets.QTableWidgetItem(str(row[1])))
        #     self.ui.tablaDetalleCompra.setItem(rowDet, 2, QtWidgets.QTableWidgetItem(str(row[2])))
        pass
    
    def vistaAdminfunction(self):
       pass

def main():
        app = QtWidgets.QApplication(sys.argv)
        form = AdminView()
        form.show()
        app.exec_()

if __name__ == '__main__':
    main()