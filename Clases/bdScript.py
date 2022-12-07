import sql

db = sql.Conexion_BD('BD/Supermark.db')

db.consulta("CREATE TABLE IF NOT EXISTS  Ventas(id_venta INTEGER PRIMARY KEY AUTOINCREMENT,id_usuario INTEGER,fecha datetime,idusuario INTEGER,FOREIGN KEY(idusuario)REFERENCES Usuario(id_usuario))")
db.consulta("CREATE TABLE IF NOT EXISTS  Usuarios(id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,email INTEGER, password VARCHAR(255),usuario VARCHAR(255),idrol INTEGER,FOREIGN KEY(idrol) REFERENCES ROL(id_rol))")
db.consulta("CREATE TABLE IF NOT EXISTS  Rol(id_rol INTEGER PRIMARY KEY AUTOINCREMENT,nombre VARCHAR(255))")
db.consulta("CREATE TABLE IF NOT EXISTS  Productos(id_producto INTEGER PRIMARY KEY AUTOINCREMENT,nombre VARCHAR(255),precio DOUBLE,stock INTEGER)")
db.consulta("CREATE TABLE IF NOT EXISTS  Ventas_Productos(id_ventP INTEGER PRIMARY KEY AUTOINCREMENT,cantidad INTEGER,precio DOUBLE,idproductos INTEGER,idventa INTEGER,FOREIGN KEY(idproductos) REFERENCES Productos(id_producto),FOREIGN KEY(idventa) REFERENCES Ventas(id_venta))")


db.cerrar()