
from peewee import *

db = SqliteDatabase('usuarios.db')

class BaseModel(Model):
    class Meta:
        database = db

class Users(BaseModel):
    #############################       campos de la DB:      ################################
    #id = AutoField(unique=True) se crea automáticamente
    nombre = CharField()
    password = CharField()

db.connect()
db.create_tables([Users])

class Verificacion():

    def comprobacion(self, usuario, contra):

        print('nombre y contraseña ingresada: {} \ {}'.format(usuario.get(), contra.get()))

        # recuperando todos los datos 
        print('usuarios existentes')
        #contador = 0
        for fila in Users.select():
            #contador += 1
            print(fila.id, fila.nombre, fila.password)
        
        try:
            #id = Users.get(Users.nombre == usuario.get()) # así devuelve id, el 1er campo
            query = Users.get(Users.nombre == usuario.get()).password # así busca por nonmbre y devuelve el password
        except:
            print('ERROR... el usuario no existe')
            query = ''

        if query  != '': # el usuario existe
            print('contraseña almacenada del usuario {}: {}'.format(usuario.get(), query))
            if query == contra.get():
                return True # si coincide usuario con contraseña
            else:
                return False
        







