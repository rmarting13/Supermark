import sql

def totalComprasRealizadas(idUsuario):
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f"SELECT COUNT(idusuario) FROM Ventas WHERE idusuario = {idUsuario}")
    db.consulta(f"SELECT id_venta FROM Ventas WHERE idusuario = {idUsuario}")
    cont=db.cursor.fetchone()
    return cont

def extrerNumerosDeCompras(idUsuario):
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f"SELECT id_venta FROM Ventas WHERE idusuario = {idUsuario}")
    lista=db.cursor.fetchall()
    return lista

def extraerUltimaVenta(idUsuario):
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f"SELECT * FROM Ventas WHERE idusuario = {idUsuario} ORDER BY id_venta DESC")
    nroCompra = db.cursor.fetchone()
    return nroCompra

def extraer_compra(nroCompra):
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f"SELECT * FROM Ventas WHERE id_venta = {nroCompra}")
    tupla = db.cursor.fetchone()
    return tupla

def agregarVentaRealizada(idusuario,fecha,productos,cantidades,subtotales,cantTotal,subtotal,descuento,total):
    productos=str(productos)
    print(type(productos))
    print(productos)
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f'INSERT INTO Ventas VALUES(NULL,"{idusuario}","{fecha}","{productos}","{cantidades}","{subtotales}","{cantTotal}","{subtotal}","{descuento}","{total}")')
    db.commit()