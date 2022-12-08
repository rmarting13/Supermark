import sql
db = sql.Conexion_BD('BD/Supermark.db')

def insertar_producto(nombre,precio,stock):
    db.consulta(f'INSERT INTO Productos VALUES(NULL,"{nombre}","{precio}","{stock}")')
    db.commit()
    db.cerrar()

def eliminar_producto(id):
    pass

def ver_productos():
    db.consulta('SELECT * FROM Productos ')
    tabla=db.cursor.fetchall()
    #print(tabla)
    return tabla
    #print(len(tabla))
    #print(len(tabla[0]))
    #una vez q tenemos el tamaño de la tabla pasamos a la interfaz el tamaño de la tabla de la interfaz
    #print(tabla[0])
    #print(tabla[0][1])
    db.cerrar()
def tamanioTabla():
    db.consulta('SELECT * FROM Productos ')
    tabla=db.cursor.fetchall()
    db.cerrar()
    return len(tabla)
    