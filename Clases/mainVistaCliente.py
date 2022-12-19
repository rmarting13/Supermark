import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPropertyAnimation , QEasingCurve , Qt
from ClientView import Ui_MainWindow
from PopUp import Dialogo
import usuarios
from HistorialCompras import HistorialCompras
import productos
import nro_compra
import Ventas_produc
import bd_ventas_produc
class ClientView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.id= " "
        self.iduser=None
        self.subtotales=[]
        self.cantidad=[]
        self.listaProduc=[]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ventanaHistorial = HistorialCompras()
        self.__limites = None
        self.__oldValues = []
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
        #permite la selección de una fila completa al hacer click en cualquier celda
        self.ui.tablaProductos.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.tablaProductos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tablaSeleccion.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tablaDetalle.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.lblSubtotalSelec.setText("0")
        self.ui.lblSubtotalImporte.setText("0")
        self.ui.lblCantTotalProdSelec.setText("0")
        self.ui.lblCantidadProductos_2.setText("0")
        self.ui.lblBonifImporte.setText("0")
        self.ui.lblTotalImporte.setText("0")
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

        #self.__cargarDatosCuenta()
        self.__cargarProductosDB()
        
        self.ui.tablaProductos.clicked.connect(self.__funcionAlClickearCeldasTablaProductos)
        
        self.ui.InicioButton.clicked.connect(self.__accionBtnInicio)
        self.ui.CuentaButton.clicked.connect(self.__accionBtnCuenta)
        self.ui.CompraButton.clicked.connect(self.__accionBtnCompra)
        self.ui.btnCerrarSesion.clicked.connect(self.__accionBtnCerrarSesion)
        self.ui.btnHistorial.clicked.connect(self.__accionBtnHistorial)
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
        self.close()

    def datos(self,id):
        self.__cargarDatosCuenta(id)
   
    def __cargarDatosCuenta(self,ide):
        #Conectar con la DB
        tupla=usuarios.Usuarios.verPerfil(ide)
        iduser=tupla[0]
        email=tupla[1]
        password=tupla[2]
        nombre=tupla[3]
        telefono=tupla[4]
        domicilio=tupla[5]
        idrol=tupla[6]
        self.iduser=iduser
        usuarioPrin=usuarios.Usuarios(iduser,email,password,nombre,telefono,domicilio,idrol)
        print(usuarioPrin)
        #print(self.id)
        print(tupla)
        self.ui.lblUsuario_2.setText(f"{nombre}")
        self.ui.lblEmail_2.setText(f"{email}")
        self.ui.lblDom_2.setText(f"{telefono}")
    
    def __cargarProductosDB(self):
       
        datos=productos.Producto.ver_productos()
        print(datos)
        print("linea 146")
        self.__completarTablaProductos(datos)



    def __completarTablaProductos(self,datos):
        lim = {}
        for item in datos:
            row = self.ui.tablaProductos.rowCount()
            self.ui.tablaProductos.insertRow(row)
            self.ui.tablaProductos.setItem(row, 0, QtWidgets.QTableWidgetItem(item[1]))
            self.ui.tablaProductos.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item[2])))
            lim[item[1]] = item[3]
        self.limites = lim #lim contiene el stock de cada producto, el cual indica el límite que puede comprar el cliente
        print(lim)

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
                self.ui.tablaSeleccion.cellWidget(row,1).lineEdit().setReadOnly(True)
                self.ui.tablaSeleccion.setItem(row,2,QtWidgets.QTableWidgetItem(str(0)))       
                self.__oldValues.append(0)
                self.ui.tablaSeleccion.cellWidget(row,1).valueChanged.connect(lambda: self.__funcionSpinBox(precio,row,self.__oldValues))
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

  
    def __funcionSpinBox(self,precio,row,oldValue):
        totalCant = int(self.ui.lblCantTotalProdSelec.text())
        subtotal = float(self.ui.lblSubtotalSelec.text())
        print(subtotal)
        newValue = self.ui.tablaSeleccion.cellWidget(row,1).value()
        if oldValue[row] < newValue: #se incrementó la cantidad (el valor del spinBox)
            if totalCant < 30:
                sub = float(precio)*newValue
                self.ui.tablaSeleccion.setItem(row,2,QtWidgets.QTableWidgetItem(str(sub)))
                cant = totalCant + 1
                suma = subtotal + float(precio)
                self.ui.lblCantTotalProdSelec.setText(str(cant))
                self.ui.lblSubtotalSelec.setText(str(suma))
            else:
                self.popUp.abrirDialogo("No se pueden seleccionar más productos!")
                newValue = newValue - 1
                self.ui.tablaSeleccion.cellWidget(row,1).stepDown()
        else:
            if newValue != oldValue[row]:
                sub = float(precio)*newValue
                self.ui.tablaSeleccion.setItem(row,2,QtWidgets.QTableWidgetItem(str(sub)))
                cant = totalCant - 1
                suma = subtotal - float(precio)
                self.ui.lblCantTotalProdSelec.setText(str(cant))
                print(suma)
                self.ui.lblSubtotalSelec.setText(str(suma))
        oldValue[row] = newValue
        if float(self.ui.lblCantTotalProdSelec.text())!=0 and self.__hayEspacioEnCarrito(float(self.ui.lblCantTotalProdSelec.text())):
                self.ui.btnAgregar.setDisabled(False)
        else:
            self.ui.btnAgregar.setDisabled(True)
            if not self.__hayEspacioEnCarrito(float(self.ui.lblCantTotalProdSelec.text())):
                self.popUp.abrirDialogo("No hay espacio suficiente en el carrito!\nReduczca la cantidad de productos.")

    def __accionBtnAgregarAlCarrito(self):
        if self.ui.tablaSeleccion.rowCount()!=0:
            datos = self.__generarListaDeTuplas(self.ui.tablaSeleccion)
            #print(datos)
            self.__completarTablaDetalle(datos)
            cant1 = int(self.ui.lblCantTotalProdSelec.text())
            cant2 = int(self.ui.lblCantidadProductos_2.text())
            self.ui.lblCantidadProductos_2.setText(str(cant1+cant2))

            self.popUp.abrirDialogo("Productos agregados con éxito!")
            self.__limpiarFormularioInicio()
            self.ui.btnConfirmar.setDisabled(False)
            self.ui.btnCancelar.setDisabled(False)
            self.__oldValues = []
        
        
    def __hayEspacioEnCarrito(self,cant):
        cant1 = int(self.ui.lblCantidadProductos_2.text())
        return (cant1+cant)<=30

    def __completarTablaDetalle(self,datos=list()):
        
        print(datos)
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
            
            #agreg
            actual=float(self.ui.lblSubtotalImporte.text()) 
            self.ui.lblSubtotalImporte.setText(f"{actual+float(sub.text())}")
            if self.ui.lblBonif_2.text().upper() == "SI":
               bonif = float(self.ui.lblSubtotalImporte.text())*0.10
            self.ui.lblBonifImporte.setText(str(bonif))
            self.ui.lblTotalImporte.setText(str(float(self.ui.lblSubtotalImporte.text())-bonif))
            self.importetotal=self.ui.lblTotalImporte.text()
   
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
        print(filas)
        return filas
    
    def __accionBtnCancelarCompra(self):
        self.popUp.abrirDialogo("Se ha cancelado la compra!")
        self.__limpiarFormularioCompras()
        
    def __eliminarFilas(self,tabla=QtWidgets.QTableWidget):
        cant = tabla.rowCount()
        for row in range(cant,-1,-1):
            tabla.removeRow(row)

    def __accionBtnConfirmarCompra(self):
        productosL = self.__generarListaDeTuplas(self.ui.tablaDetalle)
        print(usuarios.Usuarios.email)
        row=self.ui.tablaDetalle.rowCount()
        for i in range(row):
            nombreP=productosL[i][0].text()#nombre
            self.listaProduc.append(nombreP)
            cantidadP=productosL[i][1].text()#cantidad

            """----------------------------------------------------------------------------------------------"""      
            self.subtotales.append(productosL[i][2].text()) #se agregan a la lista los subtotales de cada productos
            #se agregará a la lista la cantidad correspondiente a cada producto, cuya
            self.cantidad.append(cantidadP)#posición en la lista se corresponde con la posición de cada producto en listaProd
            """----------------------------------------------------------------------------------------------"""      
          
            productos.Producto.actualizar_producto_comprado(nombreP,cantidadP)

        """----------------------------------------------------------------------------------------------"""      
        cantTotal = self.ui.lblCantidadProductos_2.text()
        subtotal = self.ui.lblSubtotalImporte.text()
        descuento = self.ui.lblBonifImporte.text()
        total = self.ui.lblTotalImporte.text()
        """----------------------------------------------------------------------------------------------"""      
        
        self.popUp.abrirDialogo("Se ha confirmado la compra!")
        self.actualizarNroDeCompra(cantTotal,subtotal,descuento,total)
        self.__limpiarFormularioCompras()

    def actualizarNroDeCompra(self,cantTotal,subtotal,desc,total):
        from datetime import date
        fechA=date.today()
        #idU=self.iduser
        #print(fechA)
        #print(idU)
        #venta1=nro_compra.Ventas(fechA,idU) 
        #venta1.agregarCompra()
        
        #print(venta1)
        #Ncompra=nro_compra.Ventas.retornarNroCompra(idU)
        #print(Ncompra)
        #print(self.listaProduc)
        #venta1.retornarNroCompra()
        venta1=Ventas_produc.ventas_produc(self.iduser,fechA,self.listaProduc,self.cantidad,self.subtotales,cantTotal,subtotal,desc,total)
        #print(venta1)
        #print("linea348")

        venta1.agregarVentaRealizada()
    
    def __accionBtnHistorial(self):
        self.ventanaHistorial.cargarHistorial(self.iduser)
        self.ventanaHistorial.show()
       
    
    def __limpiarFormularioInicio(self):
        self.__eliminarFilas(self.ui.tablaSeleccion)
        self.ui.lblCantTotalProdSelec.setText("0")
        self.ui.lblSubtotalSelec.setText("0")
        self.ui.btnAgregar.setDisabled(True)
        
    def __limpiarFormularioCompras(self):
        self.__eliminarFilas(self.ui.tablaDetalle)
        self.ui.lblSubtotalImporte.setText("0")
        self.ui.lblCantidadProductos_2.setText("0")
        self.ui.lblBonifImporte.setText("0")
        self.ui.lblTotalImporte.setText("0")
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