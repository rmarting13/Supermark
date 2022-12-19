
import sys
from PyQt5 import QtWidgets, QtGui #carga intefaz grafica
from PyQt5.QtCore import QPropertyAnimation , QEasingCurve
from AdminView import Ui_MainWindow
from PopUp import Dialogo
import usuarios
import productos
import nro_compra
import Ventas_produc
import bd_ventas_produc

class AdminView(QtWidgets.QMainWindow):
    def __init__(self):
       
        super().__init__()
        self.id= " "
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
        self.ui.tablaClientes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
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

        #self.__cargarDatosCuenta()

        self.__cargarProductosDB()

        self.__cargarUsuariosDB()
        
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
    
    def datos(self,id):
        self.__cargarDatosCuenta(id)
        

    def __cargarDatosCuenta(self,ide):
        #Conectar con la DB
        
        tupla=usuarios.Usuarios.verPerfil(ide)
        #print(self.id)
        print(tupla)
        self.ui.lblUsuario_2.setText(f"{tupla[3]}")
        self.ui.lblEmail_2.setText(f"{tupla[1]}")
        self.ui.lblDom_2.setText(f"{tupla[4]}")
    
    def __cargarProductosDB(self):

        datos=productos.Producto.ver_productos()
        print(datos)

        row = self.ui.tablaProductos.rowCount()
        for date in datos:
           self.ui.tablaProductos.insertRow(row)
           self.ui.tablaProductos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(date[1])))
           self.ui.tablaProductos.setItem(row,1,QtWidgets.QTableWidgetItem(str(date[3])))
           self.ui.tablaProductos.setItem(row, 2, QtWidgets.QTableWidgetItem(str(date[2])))
           row+=1

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

        #consulta
        producto1=productos.Producto(desc,cant,precio)
        producto1.agregar_producto()

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
        #print(desc,cant,precio)
        #extraemos el nombre seleccionado en la tabla para buscaarlo y editarlo 
        nombreC = self.ui.tablaProductos.selectedIndexes()[0].data()
        print(nombreC)
        
        self.ui.tablaProductos.setItem(selectedRow.row(),0,QtWidgets.QTableWidgetItem(desc))
        self.ui.tablaProductos.setItem(selectedRow.row(),1,QtWidgets.QTableWidgetItem(cant))
        self.ui.tablaProductos.setItem(selectedRow.row(),2,QtWidgets.QTableWidgetItem(precio))
        
        producto2=productos.Producto(desc,precio,cant)
        #datos2=producto2.ver_productos()
        print(producto2)
        producto2.actualizar_producto(nombreC) 

        self.popUp.abrirDialogo("Producto modificado con éxito!")
        self.ui.lineEditDescripcion_2.clear()
        self.ui.lineEditCantidad_2.clear()
        self.ui.lineEditPrecio_2.clear()
        self.ui.btnModificar.setDisabled(True)
    
    def __accionBtnEliminar(self):
        selectedRows = self.ui.tablaProductos.selectionModel().selectedRows()
       
        for row in selectedRows:
            self.ui.tablaProductos.removeRow(row.row())
        
        desc = self.ui.lineEditDescripcion_2.text()
        productos.Producto.eliminar_producto(desc)

        self.popUp.abrirDialogo("Producto eliminado con éxito!")
        self.ui.lineEditDescripcion_2.clear()
        self.ui.lineEditCantidad_2.clear()
        self.ui.lineEditPrecio_2.clear()
        self.ui.btnEliminar.setDisabled(True)

    def __funcionAlClickearCeldasTablaProductos(self):
        desc = self.ui.tablaProductos.selectedIndexes()[0].data()
        cant = self.ui.tablaProductos.selectedIndexes()[1].data()
        precio = self.ui.tablaProductos.selectedIndexes()[2].data()
        #print(desc,cant,precio)
        self.ui.lineEditDescripcion_2.setText(str(desc))
        self.ui.lineEditCantidad_2.setText(str(cant))
        self.ui.lineEditPrecio_2.setText(str(precio))

        self.ui.btnEliminar.setDisabled(False)
        self.ui.btnModificar.setDisabled(False)

    def __funcionAlClickearCeldasTablaClientes(self):
        #Conectar con la base de datos
        idUsuario = self.ui.tablaClientes.selectedIndexes()[3].data()
        self.__cargarDetalleDeCompra(idUsuario)
       
        
    def __cargarUsuariosDB(self):
        datosU=usuarios.Usuarios.ver_usuarios()
        print(datosU,"hola")
        #nroCompra=nro_compra.Ventas.retornarNroCompra()
        #nroCompra=nroCompra[0][0]
        #print(nroCompra,"linea 248")

        row = self.ui.tablaClientes.rowCount()
        for date in datosU:
           print(date)
           idUsuario=date[0]
           self.ui.tablaClientes.insertRow(row)
           self.ui.tablaClientes.setItem(row, 0, QtWidgets.QTableWidgetItem(str(date[3])))
           self.ui.tablaClientes.setItem(row,1,QtWidgets.QTableWidgetItem(str(date[4])))
           self.ui.tablaClientes.setItem(row, 2, QtWidgets.QTableWidgetItem(str(date[5])))
           self.ui.tablaClientes.setItem(row, 3, QtWidgets.QTableWidgetItem(str(idUsuario)))
    
    def __cargarDetalleDeCompra(self,idUsuario):
        self.__limpiarFormulario()
        tupla = bd_ventas_produc.extraerUltimaVenta(idUsuario)
        if tupla is not None:
            prod = self.__formatearStringATupla(tupla[3])
            cant = self.__formatearStringATupla(tupla[4])
            sub = self.__formatearStringATupla(tupla[5])

            print(prod)
            self.ui.lblNroCompra_2.setText(str(tupla[0]))
            self.ui.lblFechaInput.setText(tupla[2])
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
        else:
            self.popUp.abrirDialogo("El cliente seleccionado no ha\n realizado ninguna compra!")

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
        form = AdminView()
        form.show()
        app.exec_()

if __name__ == '__main__':
    main()