from usuario import*
from tarjetaCliente import*
from carrito import*

class Cliente(Usuario):
    def __init__(self,idUser,nombre,email,contra,idCliente,dom,):
        super().__init__(idUser,nombre,email,contra)
        self.__idCliente = idCliente
        self.__domicilio = dom
        self.__tarjetaCliente = None


    @property
    def idCliente(self):
        return self.__idCliente
    @idCliente.setter
    def idCliente(self,id):
        self.__idCliente = id

    @property
    def domicilio(self):
        return self.__domicilio
    @domicilio.setter
    def domicilio(self,dom):
        self.__domicilio = dom

    @property
    def tarjetaCliente(self):
        return self.__tarjetaCliente
    @tarjetaCliente.setter
    def tarjetaCliente(self,tarjeta=TarjetaCliente):
        self.__tarjetaCliente = tarjeta

    