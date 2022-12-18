import sql

def extraer_compra(nroCompra):
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f"SELECT Ventas_Productos.idproductos,Ventas_Productos.cantidad,Ventas_Productos.precio FROM Ventas_Productos INNER JOIN Ventas on Ventas.id_venta='{nroCompra}'")
    tabla=db.cursor.fetchall()
    return tabla
def agregarVentaRealizada(cantidad,precio,productos,idventa):
    productos=str(productos)
    print(type(productos))
    print(productos)
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f'INSERT INTO Ventas_Productos VALUES(NULL,"{cantidad}","{precio}","{productos}","{idventa}")')
    db.commit()