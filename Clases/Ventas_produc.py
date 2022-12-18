import bd_ventas_produc
class ventas_produc:
    def __init__(self,cantidad,precio,idproductos, idventa):
        #self.__idventP = idventP
        self.__cantidad = cantidad
        self.__precio = precio
        self.__idproductos = idproductos
        self.__idventa = idventa
    def __str__(self):
        return f"""
        cantidad={self.__cantidad}
        precio = {self.__precio}
        idproductos = {self.__idproductos}
        idventa={self.__idventa}
        """
    def consultar_compra_porNro(nroCompra):
        return bd_ventas_produc.extraer_compra(nroCompra)
    def agregarVentaRealizada(self):
        print(self.__cantidad,self.__precio,self.__idproductos,self.__idventa)
        bd_ventas_produc.agregarVentaRealizada(self.__cantidad,self.__precio,self.__idproductos,self.__idventa)