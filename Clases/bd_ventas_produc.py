import sql

def extraer_compra(nroCompra):
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f"SELECT Ventas_Productos.idproductos,Ventas_Productos.cantidad,Ventas_Productos.precio FROM Ventas_Productos INNER JOIN Ventas on Ventas.id_venta='{nroCompra}'")
    tabla=db.cursor.fetchall()
    return tabla