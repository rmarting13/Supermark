from usuario import*

class Admin(Usuario):
    def __init__(self,idUser,nombre,email,contra,idAdmin):
        super().__init__(idUser,nombre,email,contra)
        self.__idAdmin = idAdmin

@property
def idAdmin(self):
    return self.__idAdmin
@idAdmin.setter
def idAdmin(self,id):
    self.__idAdmin = id