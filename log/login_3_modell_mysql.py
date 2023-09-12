from tkinter import *
from peewee import *

db = MySQLDatabase(host="localhost", user="root", passwd="sofocles11", database="db_usuarios_old")


class BaseModel(Model):
    class Meta:
        database = db

class Users(BaseModel):
    #############################  nombre de la Tabla: Users
    #############################  campos:
    idUsers = AutoField(unique=True)    # con MySql hay que escribir este campo
                                        # (a diferencia de Sqlite, no se puede omitir))
    name = CharField()
    password = CharField()

db.connect()
#db.create_tables([Users])

class User_actual:
    def __init__(self, nombre='', clave=''):
        self.name = nombre
        self.password = clave
        self.conected = False
        self.intentos = 3 # number of attempts you will have to log in

    def verificar(self, ): #usuario, contra):
        print('se ingreso -> nombre: {} y -> contraseña: {}'.format(self.name, self.password))
        ############################################
        print('usuarios existentes: \n--------------------')
        for fila in Users.select():
            print(fila.idUsers, fila.name, fila.password)
        ############################################
        try:
            #query=''
            query = Users.get(Users.name == self.name).password # así busca por nonmbre y devuelve el password
        except:
            print('ERROR... el usuario no existe')
            query = ''
        if query  != '': # el usuario existe
            #print('contraseña almacenada del usuario {}: {}'.format(self.name, query))
            print('contraseña ingresada: {}'.format(self.password))
            if query == self.password:
                return True # si coincide usuario con contraseña
            else:
                return False
        
    # def desconectar(self):
    #     print('-'*100)
    #     if self.conected:
    #         print("Se cerro sesion con exito!!")
    #         self.conected = False
    #     else:
    #         print("Error, aún no inició sesion")
    #     print('-'*100)


