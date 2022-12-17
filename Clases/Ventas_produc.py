class ventas_produc:
    def __init__(self,precio,idproductos, idventa):
        #self.__idventP = idventP
        self.__precio = precio
        self.__idproductos = idproductos
        self.__idventa = idventa
    def __str__(self):
        return f"""
        precio = {self.__precio}
        idproductos = {self.__idproductos}
        idventa={self.__idventa}
        """