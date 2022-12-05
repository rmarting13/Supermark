class Usuario:
    def __init__(self,id,nombre,email,contra):
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__contra = contra

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        self.__email = email
    
    @property
    def contra(self):
        return self.__contra
    @contra.setter
    def contra(self,contra):
        self.__contra = contra

