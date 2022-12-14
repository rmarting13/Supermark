import bd_Usuarios

class Usuarios:
    def __init__(self,id_usuario,email,password,nombre,domicilio,telefono,idrol=1):
        self.__id_usuario =id_usuario
        self.__email = email
        self.__password = password
        self.__nombre =nombre
        self.__domicilio = domicilio
        self.__telefono = telefono
        self.__idrol = idrol
    @property
    def id_usuario(self):
        return self.__id_usuario
    @id_usuario.setter
    def id_usuario(self,id_usuario):
        self.__id_usuario = id_usuario
    @property
    def email(self):
        return self.__email
    @property
    def password(self):
        return self.__password
    @property
    def nombre(self):
        return self.__nombre
    @property
    def domicilio(self):
        return self.__domicilio
    @property
    def telefono(self):
        return self.__telefono
    @property
    def idrol(self):
        return self.__idrol
    @email.setter
    def email(self,email):
        self.__email = email
    @password.setter
    def password(self,password):
        self.__password = password
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    @domicilio.setter
    def domicilio(self,domicilio):
        self.domicilio = domicilio
    @telefono.setter
    def telefono(self,telefono):
        self.telefono = telefono
    @idrol.setter
    def idrol(self,idrol):
        self.__idrol = idrol
    
    def verPerfil(id):
        print(id)
        return bd_Usuarios.verPerfil(id)
    def ver_usuarios():
        return bd_Usuarios.ver_usuarios()
    def __str__(self):
        return f"""
        email = {self.__email}
        nombre = {self.__nombre}
        """