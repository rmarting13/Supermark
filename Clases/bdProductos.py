import sql

#db = sql.Conexion_BD('BD/Supermark.db')
def insertar_producto(nombre,precio,stock):
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f'INSERT INTO Productos VALUES(NULL,"{nombre}","{precio}","{stock}")')
    db.commit()
    

def eliminar_producto(id):
    print(f"el id a eliminar es {id}")
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f"DELETE FROM Productos WHERE id_producto ={id}")
    db.commit()
    
def ver_productos():
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta('SELECT * FROM Productos ')
    tabla=db.cursor.fetchall()
    return tabla

def tamanioTabla():
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta('SELECT * FROM Productos ')
    tabla=db.cursor.fetchall()
    return len(tabla)
def actualizar_producto(id,nombre,precio,stock):
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f"UPDATE Productos SET nombre='{nombre}',stock={stock},precio={precio} WHERE id_producto = {id}")
    db.commit()
    
   
def cerrar():
    db = sql.Conexion_BD('BD/Supermark.db')
    db.cerrar()

def verUnsoloProd(id):
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f'SELECT * FROM Productos WHERE id_producto ={id}')
    tabla=db.cursor.fetchall()
    return tabla
