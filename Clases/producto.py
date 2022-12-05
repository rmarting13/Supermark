class Producto:
    def __init__(self):
        self._codigo =0
        self.nombre = ''
        self.cantidad = 0
        self.precio = 0.0
        self.categoria = ''
  
    def codigo(self):
        return self._codigo
  
    def codigo(self,codigo):
        self._codigo = codigo

    def ingresar_datos(self):
        self.nombre = input("Ingresar nombre: ")
        self.cantidad = int(input("Ingresar cantidad: "))
        self.precio = float(input("Ingresar precio: "))
        self.categoria = input("ingresar categoria: ")
  
    def definir_producto(self,tupla):
        self._codigo = tupla[0][0]
        self.nombre = tupla[0][1]
        self.cantidad = tupla[0][2]
        self.precio = tupla[0][3]
        self.categoria = tupla[0][4]
  
    def editar(self):
        print(f"Nombre: {self.nombre}")
        valor = input("Ingresar nombre: ")
        if valor != '':
            self.nombre = valor
        print(f"Cantidad: {self.cantidad}")
        try:
            valor = int(input("Ingresar cantidad: "))
        except:
            valor = 0
        if valor != 0:
            self.cantidad = valor
        print(f"Precio: ${self.precio}")
        try:
            valor = float(input("Ingresar precio: "))
        except:
            valor = 0
        if valor != 0:
            self.precio = valor
        print(f"Categoria: {self.categoria}")
        valor = input("Ingresar categoria: ")
        if valor != '':
            self.categoria = valor
  
    def __str__(self):
        return f"""
        Nombre = {self.nombre}
        Cantidad = {self.cantidad}
        Precio = {self.precio}
        Categoria = {self.categoria}
        """