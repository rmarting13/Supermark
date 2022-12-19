import bd_ventas_produc
class ventas_produc:
    def __init__(self,idusuario,fecha_v,idproductos,cantidades,subtotales,cantTotal,subtotal,descuento,total):
        #self.__idventP = idventP
        self.__fecha_v = fecha_v
        self.__idusuario = idusuario
        self.__cantidades = cantidades
        self.__subtotales = subtotales
        self.__idproductos = idproductos
        self.__cantTotal = cantTotal
        self.__subtotal = subtotal
        self.__desc = descuento
        self.__total = total
    def __str__(self):
        return f"""
        idventa={self.__idusuario}
        fecha = {self.__fecha_v}
        idproductos = {self.__idproductos}
        cantidades={self.__cantidades}
        subtotales = {self.__subtotales}
        cantTotal = {self.__cantTotal}
        subtotal = {self.__subtotal}
        descuento = {self.__desc}
        total = {self.__total}
        """
    def consultarCantComprasRealizadas(idUsuario):
        return bd_ventas_produc.totalComprasRealizadas(idUsuario)
    def consultar_compra_porNro(nroCompra):
        return bd_ventas_produc.extraer_compra(nroCompra)

    def agregarVentaRealizada(self):
        print(self.__cantidades,self.__subtotales,self.__idproductos)
        bd_ventas_produc.agregarVentaRealizada(self.__idusuario,self.__fecha_v,self.__idproductos,self.__cantidades,self.__subtotales,self.__cantTotal,self.__subtotal,self.__desc,self.__total)