import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPropertyAnimation , QEasingCurve , Qt
from PopUp import Dialogo
from ClientView import Ui_MainWindow

class UiPrincipal(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow
        self.popUp = Dialogo()

    def expandir(self,frame=QtWidgets.QFrame,btn=QtWidgets.QPushButton):
        ancho = frame.width()
        if ancho == 50:
            nuevoAncho = 140
            btn.setIcon(QtGui.QIcon("interfaces/icons/arrow-left-44.png"))
        elif ancho == 140:
            nuevoAncho = 50
            btn.setIcon(QtGui.QIcon("interfaces/icons/bars.png"))

        try:
            self.animacion = QPropertyAnimation(frame,b"minimumWidth")
            self.animacion.setStartValue(ancho)
            self.animacion.setEndValue(nuevoAncho)
            self.animacion.setDuration(350)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()
        except:
            btn.setIcon(QtGui.QIcon("interfaces/ui/icons/bars.png"))
            self.animacion.setStartValue(50)
            self.animacion.setEndValue(50)
            self.animacion.setDuration(350)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()
    


    #Modos: 0 - btnInicio , 1 - btnCuenta, any - btnCompras/btnInventario
    def funcionPushBtn(self,ui=Ui_MainWindow,modo=int):
        if modo == 0:

            self.ui.InicioButton.setStyleSheet(color.replace("transparent","#ffdd52"))
            self.ui.CuentaButton.setStyleSheet(self.ui.CuentaButton.styleSheet().replace("#1aa7ff","transparent"))
            self.ui.CompraButton.setStyleSheet(self.ui.CompraButton.styleSheet().replace("#8ebf19","transparent"))
        elif modo == 1:
            self.ui.CuentaButton.setStyleSheet(color.replace("transparent","#1aa7ff"))
            self.ui.InicioButton.setStyleSheet(self.ui.InicioButton.styleSheet().replace("#ffdd52","transparent"))
            self.ui.CompraButton.setStyleSheet(self.ui.CompraButton.styleSheet().replace("#8ebf19","transparent"))
        else:
            self.ui.CompraButton.setStyleSheet(color.replace("transparent","#8ebf19"))
            self.ui.InicioButton.setStyleSheet(self.ui.InicioButton.styleSheet().replace("#ffdd52","transparent"))
            self.ui.CuentaButton.setStyleSheet(self.ui.CuentaButton.styleSheet().replace("#1aa7ff","transparent"))

    def __accionBtnPrincipal1(ui):
        self.ui.Paginas.setCurrentWidget(self.ui.PaginaInicio)
        color = self.ui.InicioButton.styleSheet()
        self.ui.InicioButton.setStyleSheet(color.replace("transparent","#ffdd52"))
        self.ui.CuentaButton.setStyleSheet(self.ui.CuentaButton.styleSheet().replace("#1aa7ff","transparent"))
        self.ui.CompraButton.setStyleSheet(self.ui.CompraButton.styleSheet().replace("#8ebf19","transparent"))
    
    def __accionBtnPrincipal2(self):
        self.ui.Paginas.setCurrentWidget(self.ui.PaginaCuenta)
        color = self.ui.CuentaButton.styleSheet()
        self.ui.CuentaButton.setStyleSheet(color.replace("transparent","#1aa7ff"))
        self.ui.InicioButton.setStyleSheet(self.ui.InicioButton.styleSheet().replace("#ffdd52","transparent"))
        self.ui.CompraButton.setStyleSheet(self.ui.CompraButton.styleSheet().replace("#8ebf19","transparent"))
        
    def __accionBtnPrincipal3(self):
        self.ui.Paginas.setCurrentWidget(self.ui.PaginaComprar)
        color = self.ui.CompraButton.styleSheet()
        self.ui.CompraButton.setStyleSheet(color.replace("transparent","#8ebf19"))
        self.ui.InicioButton.setStyleSheet(self.ui.InicioButton.styleSheet().replace("#ffdd52","transparent"))
        self.ui.CuentaButton.setStyleSheet(self.ui.CuentaButton.styleSheet().replace("#1aa7ff","transparent"))

    def accionBtnCerrarSesion(self):
        #llamar al método que inicia la ui de registro
        self.close()