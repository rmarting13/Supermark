import sqlite3

class Conexion_BD():
#timeout=10
    def __init__(self,bd):#bd es el nombre de la base de datos
        self.conexion = sqlite3.connect(bd,timeout=10)
        self.cursor = self.conexion.cursor()

    def consulta(self, consulta):
        self.cursor.execute(consulta)
    
    def commit(self):
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()