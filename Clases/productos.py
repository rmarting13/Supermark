import bd_Productos
class Producto:
    def __init__(self,nombre,precio,stock,id=1):
        self.__nombre =nombre
        self.__precio = precio
        self.__stock=stock
        self.__id=id
    @property
    def id(self):
        return self.__id
    @property
    def nombre(self):
        return self.__nombre
    @property
    def precio(self):
        return self.__precio
    @property
    def stock(self):
        return self.__stock
    @id.setter
    def id(self, id):
        self.__id = id
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    @precio.setter
    def precio(self,precio):
        self.__precio=precio
    @stock.setter
    def stock(self,stock):
        self.__stock=stock
  
    def agregar_producto(self):
        bd_Productos.insertar_producto(self.__nombre,self.__precio,self.__stock)
    def ver_productos():
        return bd_Productos.ver_productos()

    def eliminar_producto(nombre):
        bd_Productos.eliminar_producto(nombre)

    def actualizar_producto(self,nombreC):
        bd_Productos.actualizar_producto(self.__nombre,self.__stock,self.__precio,nombreC)
    def actualizar_producto_comprado(nombreP,cantidadP):
        bd_Productos.actualizar_producto_comprado(nombreP,cantidadP)
    def __str__(self):
        return f"""
        Nombre = {self.__nombre}
        stock = {self.__stock}
        Precio = {self.__precio}
        """