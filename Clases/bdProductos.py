import sql
db = sql.Conexion_BD('BD/Supermark.db')

def insertar_producto(nombre,precio,stock):
    db.consulta(f'INSERT INTO Productos VALUES(NULL,"{nombre}","{precio}","{stock}")')
    db.commit()
    db.cerrar()