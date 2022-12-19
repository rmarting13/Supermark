import sql
def insertar_producto(nombre,precio,stock):
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f'INSERT INTO Productos VALUES(NULL,"{nombre}","{precio}","{stock}")')
    db.commit()
    
def ver_productos():
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta('SELECT * FROM Productos ')
    tabla=db.cursor.fetchall()
    return tabla

def eliminar_producto(nombre):
    print(f"el producto a eliminar es {nombre}")
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f"DELETE FROM Productos WHERE nombre='{nombre}'")
    db.commit()

def actualizar_producto(nombre,stock,precio,nombreC):
    print(nombre,stock,precio,nombreC)
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f"UPDATE Productos SET nombre='{nombre}', stock='{stock}', precio='{precio}' WHERE nombre ='{nombreC}'")
    db.commit()
    print("consulta echa")

def actualizar_producto_comprado(nombre,cantidad):
    print(nombre,cantidad)
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f"UPDATE Productos SET stock=stock-'{cantidad}' WHERE nombre ='{nombre}'")
    db.commit()
    print("consulta echa")