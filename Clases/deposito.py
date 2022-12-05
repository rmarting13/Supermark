class Deposito:
    def __init__(self):
        self.__admin = ""
        self.__listaProductos = ""

    def getAdministrador(self):
        return self.__administrador

    def setAdministrador(self,admin):
        self.__admin = admin

    def getProductos(self):
        return self.__listaProductos

    def consultarStock(self,prod):
        pass

    def cargarProductos(self,productos):
        self.__listaProductos = productos

    