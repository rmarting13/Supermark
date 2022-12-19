import sql 
def retorna_nroCompra(iduser):
    db=sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f"SELECT Max(Ventas.id_venta),Ventas.fecha,Ventas.idusuario FROM Ventas INNER JOIN Usuarios on Ventas.idusuario='{iduser}'")
    tabla=db.cursor.fetchall()
    return tabla
def agregar_compra(fecha,idusuario):
    db= sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f'INSERT INTO Ventas VALUES(NULL,"{fecha}","{idusuario}")')
    db.commit()