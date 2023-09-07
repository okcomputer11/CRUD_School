from os import name
from tkinter import *

from peewee import *

#db = MySQLDatabase(host="localhost", user="root", passwd="sofocles11", database="School")
db = SqliteDatabase('usuarios.db')

class BaseModel(Model):
    class Meta:
        database = db

class Users(BaseModel):
    #############################       campos de la DB:      ################################
    #id = AutoField(unique=True) se crea automáticamente
    nombre = CharField()
    password = CharField()

    ############# cambiar nombre x name después!!!!!

db.connect()
db.create_tables([Users])

class User_actual:
    def __init__(self, nombre='', clave=''):
        self.name = nombre
        self.password = clave
        self.conected = False
        self.intentos = 5

    def verificar(self, ): #usuario, contra):
        print('se ingresaron -> nombre: {} y -> contraseña: {}'.format(self.name, self.password))
        print('usuarios existentes:')
        #contador = 0
        for fila in Users.select():
            #contador += 1
            print(fila.id, fila.nombre, fila.password)
        try:
            query = Users.get(Users.nombre == self.name).password # así busca por nonmbre y devuelve el password
        except:
            print('ERROR... el usuario no existe')
            query = ''
        if query  != '': # el usuario existe
            print('contraseña almacenada del usuario {}: {}'.format(self.name, query))
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


