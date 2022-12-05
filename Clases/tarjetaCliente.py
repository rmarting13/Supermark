from cliente import*

class TarjetaCliente:
    def __init__(self,nro,cliente=Cliente,dto=5):
        self.__nro = nro
        self.__cliente = cliente
        self.__descuento = dto

    @property
    def nro(self):
        return self.__nro
    @nro.setter
    def nro(self,nro):
        self.__nro = nro
    
    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self,cliente = Cliente):
        self.__cliente = cliente
    
    @property
    def descuento(self):
        return self.__descuento
    @descuento.setter
    def descuento(self,dto):
        self.__descuento = dto