from PyQt5 import QtSql

class conexion_BD():
    def __init__(self,bd):
        self.db= QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(bd)
        if not self.db.open():
            print("error")
        self.query = QtSql.QSqlQuery()
        print('fin')

    def consulta(self,email,password):
        self.query.exec_("SELECT * FROM Usuarios as U INNER JOIN Rol as R ON U.idrol=R.id_rol where email = '%s' and password='%s';"%(email, password))
        self.query.first()
        if self.query.value("email") != None and self.query.value("password")!= None:
            print("se ingreso exitosamente")
            #if self.query.value('nombre')=='admin':
            #     self.admin.show()
            #else:
            #     self.cliente.show()

        else:
            print("error al ingresar")
             #self.usuario.clear()
             #self.password.clear()
    def consulta2(self,nombre,direccion,telefono,email,password):
        print(nombre,direccion,telefono,email,password)
        self.query.exec_(f'INSERT INTO Usuarios VALUES (NULL,"{email}","{password}","{nombre}","{direccion}","{telefono}",2)')
        print("Hola")
       #self.db.commit()
    