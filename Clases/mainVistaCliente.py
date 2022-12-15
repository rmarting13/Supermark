import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPropertyAnimation , QEasingCurve , Qt
from ClientView import Ui_MainWindow
from PopUp import Dialogo

class ClientView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__limites = None
        self.setupUiComponents()
        self.popUp = Dialogo()
        #self.db = db conectar con la base de datos
        self.ui.MenuButton.clicked.connect(self.expandir)

    @property
    def limites(self):
        return self.__limites

    @limites.setter
    def limites(self,lim):
        self.__limites = lim

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
        #TIP: crear una lista para almacenar cada fila de la base de datos, luego pasarlas como parámetros
        #por referencia a los generadores de las tablas de la UI, de modo que las modificaciones realizadas
        #en los elementos de las tablas impacten en forma directa sobre el contenido de las listas, para luego
        #volver a enviar las mismas listas a la base de datos para actualizar su contenido.
        
        #self.__completarTablaProductos(self.db.consultaFetchAll)
        
        """------------------------------------------------------------------------------------------------"""
        #El siguiente bloque de código agrega 2 productos a la tabla productos a modo de ejemplo, eliminar
        #una vez conectada la base de datos
        lim = {}
        row = self.ui.tablaProductos.rowCount()
        self.ui.tablaProductos.insertRow(row)
        self.ui.tablaProductos.setItem(row, 0, QtWidgets.QTableWidgetItem("Papas"))
        self.ui.tablaProductos.setItem(row, 1, QtWidgets.QTableWidgetItem("250"))
        lim["Papas"] = 35
        row = self.ui.tablaProductos.rowCount()
        self.ui.tablaProductos.insertRow(row)
        self.ui.tablaProductos.setItem(row, 0, QtWidgets.QTableWidgetItem("Merca"))
        self.ui.tablaProductos.setItem(row, 1, QtWidgets.QTableWidgetItem("760"))
        lim["Merca"] = 15
        self.limites = lim
        """------------------------------------------------------------------------------------------------"""

    def __completarTablaProductos(self,datos=list):
        lim = {}
        for item in datos:
            row = self.ui.tablaProductos.rowCount()
            self.ui.tablaProductos.insertRow(row)
            self.ui.tablaProductos.setItem(row, 0, QtWidgets.QTableWidgetItem(item[1]))
            self.ui.tablaProductos.setItem(row, 1, QtWidgets.QTableWidgetItem(item[3]))
            lim[item[1]] = item[2]
        self.limites = lim #lim contiene el stock de cada producto, el cual indica el límite que puede comprar el cliente


    def __funcionAlClickearCeldasTablaProductos(self):
        if int(self.ui.lblCantTotalProdSelec.text()) < 30:
            desc = self.ui.tablaProductos.selectedIndexes()[0].data()
             #evita que se seleccione un producto ya agregado
            if not self.__productoAgregado(self.ui.tablaSeleccion,desc):
                precio = self.ui.tablaProductos.selectedIndexes()[1].data()
                row = self.ui.tablaSeleccion.rowCount()
                self.ui.tablaSeleccion.insertRow(row)
                self.ui.tablaSeleccion.setItem(row,0,QtWidgets.QTableWidgetItem(desc))
                maxim = min(int(self.limites[desc]),30) #Determina el máximo stock disponible para comprar
                #agrega una columna con QSpinBox
                self.ui.tablaSeleccion.setCellWidget(row,1,QtWidgets.QSpinBox(minimum=0,maximum=maxim))
                self.ui.tablaSeleccion.setItem(row,2,QtWidgets.QTableWidgetItem(str(0)))       
                self.ui.tablaSeleccion.cellWidget(row,1).valueChanged.connect(lambda: self.__funcionSpinBox(precio,row))
        else:
             self.popUp.abrirDialogo("No se pueden seleccionar más productos!")

    def __productoAgregado(self,tabla=QtWidgets.QTableWidget,prod=str):
        if tabla.rowCount()!=0:
            productos=[]
            for i in range(tabla.rowCount()):
                productos.append(tabla.item(i,0).text())
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

    def __haySuficienteStock(self,row,valor):
        prod = self.ui.tablaSeleccion.item(row,0).text()
        return self.limites[prod] >= valor


    def __accionBtnAgregarAlCarrito(self):
        if self.ui.tablaSeleccion.rowCount()!=0:
            datos = self.__generarListaDeTuplas(self.ui.tablaSeleccion)
            self.__completarTablaDetalle(datos)
            self.popUp.abrirDialogo("Productos agregados con éxito!")
            self.__limpiarFormularioInicio()
            self.ui.btnConfirmar.setDisabled(False)
            self.ui.btnCancelar.setDisabled(False)

        # if self.ui.tablaSeleccion.rowCount()!=0:
        #     suma = 0; bonif = 0
        #     for row in range(0,self.ui.tablaSeleccion.rowCount()):
        #         if self.ui.tablaSeleccion.item(row,2).text() != "0":
        #             desc = self.ui.tablaSeleccion.item(row,0).clone()
        #             cant = self.ui.tablaSeleccion.cellWidget(row,1).value()
        #             sub = self.ui.tablaSeleccion.item(row,2).clone()
        #             if not self.__productoAgregado(self.ui.tablaDetalle,desc.text()):
        #                 rowDet = self.ui.tablaDetalle.rowCount()
        #                 self.ui.tablaDetalle.insertRow(rowDet)
        #                 self.ui.tablaDetalle.setItem(rowDet, 0, desc)
        #                 self.ui.tablaDetalle.setItem(rowDet, 1, QtWidgets.QTableWidgetItem(str(cant)))
        #                 self.ui.tablaDetalle.setItem(rowDet, 2, sub)
        #             else:
        #                 items = self.ui.tablaDetalle.findItems(desc.text(),Qt.MatchExactly)
        #                 ind = self.ui.tablaDetalle.row(items[0])
        #                 nuevoCant = int(self.ui.tablaDetalle.item(ind,1).text()) + int(cant)
        #                 nuevoSub = float(self.ui.tablaDetalle.item(ind,2).text()) + float(sub.text())
        #                 self.ui.tablaDetalle.item(ind,1).setText(str(nuevoCant))
        #                 self.ui.tablaDetalle.item(ind,2).setText(str(nuevoSub))                   
        #             suma = suma+float(sub.text())
        #     actual = float(self.ui.lblSubtotalImporte.text())
        #     self.ui.lblSubtotalImporte.setText(f"{actual+suma}")
        #     if self.ui.lblBonif_2.text().upper() == "SI":
        #         bonif = float(self.ui.lblSubtotalImporte.text())*0.10
        #     self.ui.lblBonifImporte.setText(str(bonif))
        #     self.ui.lblTotalImporte.setText(str((actual+suma)-bonif))
            #Se limpia la lista de productos seleccionados para evitar agregar productos repetidos en el carrito
            #self.popUp.abrirDialogo("Productos agregados con éxito!")
            #self.__limpiarFormularioInicio
            # self.__eliminarFilas(self.ui.tablaSeleccion)
            # self.ui.lblCantTotalProdSelec.setText("0")
            # self.ui.lblSubtotalSelec.setText("0")
            # self.ui.btnAgregar.setDisabled(True)
            # self.ui.btnConfirmar.setDisabled(False)
            # self.ui.btnCancelar.setDisabled(False)
        
    def __completarTablaDetalle(self,datos=list):
        suma = 0; bonif = 0
        for row in datos:
            if row[2].text() != "0":
                desc = row[0]
                cant = row[1]
                sub = row[2]
                if not self.__productoAgregado(self.ui.tablaDetalle,desc.text()):
                    rowDet = self.ui.tablaDetalle.rowCount()
                    self.ui.tablaDetalle.insertRow(rowDet)
                    self.ui.tablaDetalle.setItem(rowDet, 0, desc)
                    self.ui.tablaDetalle.setItem(rowDet, 1, cant)
                    self.ui.tablaDetalle.setItem(rowDet, 2, sub)
                else:
                    items = self.ui.tablaDetalle.findItems(desc.text(),Qt.MatchExactly)
                    ind = self.ui.tablaDetalle.row(items[0]) #Nos interesa la primera aparición
                    nuevoCant = int(self.ui.tablaDetalle.item(ind,1).text()) + int(cant.text())
                    nuevoSub = float(self.ui.tablaDetalle.item(ind,2).text()) + float(sub.text())
                    self.ui.tablaDetalle.item(ind,1).setText(str(nuevoCant))
                    self.ui.tablaDetalle.item(ind,2).setText(str(nuevoSub))                   
                suma = suma+float(sub.text())
            actual = float(self.ui.lblSubtotalImporte.text())
            self.ui.lblSubtotalImporte.setText(f"{actual+suma}")
            if self.ui.lblBonif_2.text().upper() == "SI":
                bonif = float(self.ui.lblSubtotalImporte.text())*0.10
            self.ui.lblBonifImporte.setText(str(bonif))
            self.ui.lblTotalImporte.setText(str((actual+suma)-bonif))

    def __generarListaDeTuplas(self,tabla=QtWidgets.QTableWidget):
    #Retorna los elementos de una tabla en formato de lista de tuplas, donde cada tupla de la lista
    #es una fila, y cada elemento de la tupla (fila) es una columna
        filas = []
        for row in range(tabla.rowCount()):
            columnas = []
            for col in range(tabla.columnCount()):
                if isinstance(tabla.cellWidget(row,col),QtWidgets.QSpinBox):
                    cant = str(tabla.cellWidget(row,col).value())
                    columnas.append(QtWidgets.QTableWidgetItem(cant))
                else:
                    columnas.append((tabla.item(row,col)).clone())
            filas.append(tuple(columnas))
        return filas
    
    def __accionBtnCancelarCompra(self):
        self.popUp.abrirDialogo("Se ha cancelado la compra!")
        self.__limpiarFormularioCompras()
        
    def __eliminarFilas(self,tabla=QtWidgets.QTableWidget):
        cant = tabla.rowCount()
        for row in range(cant,-1,-1):
            tabla.removeRow(row)

    def __accionBtnConfirmarCompra(self):
        """------------------------------------------------------------------------------------------------"""
        #En productos se almacena la lista de tuplas que representa la lista de productos comprados
        productos = self.__generarListaDeTuplas(self.ui.tablaDetalle)
        #trabajar con esta tupla para actualizar la base de datos, recordar que los elementos de las tuplas
        #son del tipo QTableWidgetItem, cuyo método para obtener el dato es productos[indice1][indice2].text()
        #donde indice1 es la fila y indice2 es la columna. También recordar que la columna 0 es el nombre (descripción)
        #del producto (ver tabla Detalle de compra)
        #Realizar las consultas para dar de baja los productos comprados.
        """------------------------------------------------------------------------------------------------"""
        
        self.popUp.abrirDialogo("Se ha confirmado la compra!")    
        self.__limpiarFormularioCompras()
    

    
    def __limpiarFormularioInicio(self):
        self.__eliminarFilas(self.ui.tablaSeleccion)
        self.ui.lblCantTotalProdSelec.setText("0")
        self.ui.lblSubtotalSelec.setText("0")
        self.ui.btnAgregar.setDisabled(True)

    def __limpiarFormularioCompras(self):
        self.__eliminarFilas(self.ui.tablaDetalle)
        self.ui.lblSubtotalImporte.setText("0")
        self.ui.lblBonifImporte.clear()
        self.ui.lblTotalImporte.clear()
        self.ui.btnCancelar.setDisabled(True)
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