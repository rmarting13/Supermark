import bdProductos
class Producto:
    def __init__(self,nombre,precio,stock):
        self.__nombre =nombre
        self.__precio = precio
        self.__stock=stock
    @property
    def nombre(self):
        return self.__nombre
    @property
    def precio(self):
        return self.__precio
    @property
    def stock(self):
        return self.__stock
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
        bdProductos.insertar_producto(self.__nombre,self.__precio,self.__stock)
    
    # def ingresar_datos(self):
    #     self.nombre = input("Ingresar nombre: ")
    #     self.cantidad = int(input("Ingresar cantidad: "))
    #     self.precio = float(input("Ingresar precio: "))
    #     self.categoria = input("ingresar categoria: ")
  
    # def definir_producto(self,tupla):
    #     self._codigo = tupla[0][0]
    #     self.nombre = tupla[0][1]
    #     self.cantidad = tupla[0][2]
    #     self.precio = tupla[0][3]
    #     self.categoria = tupla[0][4]
  
    # def editar(self):
    #     print(f"Nombre: {self.nombre}")
    #     valor = input("Ingresar nombre: ")
    #     if valor != '':
    #         self.nombre = valor
    #     print(f"Cantidad: {self.cantidad}")
    #     try:
    #         valor = int(input("Ingresar cantidad: "))
    #     except:
    #         valor = 0
    #     if valor != 0:
    #         self.cantidad = valor
    #     print(f"Precio: ${self.precio}")
    #     try:
    #         valor = float(input("Ingresar precio: "))
    #     except:
    #         valor = 0
    #     if valor != 0:
    #         self.precio = valor
    #     print(f"Categoria: {self.categoria}")
    #     valor = input("Ingresar categoria: ")
    #     if valor != '':
    #         self.categoria = valor
  
    def __str__(self):
        return f"""
        Nombre = {self.__nombre}
        stock = {self.__stock}
        Precio = {self.__precio}
        """