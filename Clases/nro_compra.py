import bd_nro_compra
class Ventas:
    def __init__(self,fecha_v,idusuario):
        self.fecha_v = fecha_v
        self.idusuario = idusuario

    def __str__(self):
        return f"""
        fecha = {self.fecha_v}
        id_usuario = {self.idusuario}
        """
    def retornarNroCompra(iduser):
        return bd_nro_compra.retorna_nroCompra(iduser)
    