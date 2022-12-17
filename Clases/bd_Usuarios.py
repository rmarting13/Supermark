import sql

def verPerfil(id):
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta(f'SELECT * FROM Usuarios WHERE id_usuario ={id}')
    tabla=db.cursor.fetchall()
    #db.commit()
    return tabla
def ver_usuarios():
    db = sql.Conexion_BD('BD/Supermark.db')
    db.consulta('SELECT * FROM Usuarios WHERE idrol=2')
    tabla=db.cursor.fetchall()
    return tabla