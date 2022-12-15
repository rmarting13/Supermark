import sql

def verPerfil(id):
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f'SELECT * FROM Usuarios WHERE id_usuario ={id}')
    tabla=db.cursor.fetchall()
    #db.commit()
    return tabla
