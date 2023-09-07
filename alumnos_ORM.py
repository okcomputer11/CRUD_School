from peewee import *
from tkinter import *
import csv
import time

db = SqliteDatabase('Schule.db') # contiene la tabla "Students"

# Falta implementar "Buscar alumno x nombre"
# Falta implementar "Buscar alumno x dni"

class BaseModel(Model):
    class Meta:
        database = db

class Students(BaseModel): # campos de la DB:  
    #id = AutoField(unique=True) se crea automáticamente # oder register = int 
    dni = CharField()
    class_division = CharField()
    first_name = CharField()
    last_name = CharField()
    day_birth = CharField()
    status = CharField()
    sexo = CharField()
    address = CharField()
    line_phone = CharField()
    movile_phone1 = CharField()
    movile_phone2 = CharField()

db.connect()
db.create_tables([Students])

##################################################################################################

class Loggeo():
    def __init__(self,): # usuario_logeado):
        self.nombre = ''
        self.accion = ''        # acciones que realiza sobre la base de datos: login / alta, baja, modificacion
        self.id_afectado = ''   # a cuál alumno le realiza la acción
        self.fecha = ''         # fecha y hora de la accion
        self.hora = ''   
        # #####################
        # line = (self.nombre, self.accion, self.id_afectado, self.fecha, self.hora)
        # graba_log(line)
        # #####################

usuario_global = Loggeo()

def graba_log():

    line = [usuario_global.nombre, usuario_global.accion, usuario_global.id_afectado]
    print('id a afectar:', usuario_global.id_afectado)
    print('Graba Log')
    print('---------')
    #print('fecha y hora:', datetime.datetime.strftime('%Y/%m/%d %H:%M:%S'))
    usuario_global.fecha = time.strftime('%Y/%m/%d')
    usuario_global.hora = time.strftime('%H:%M:%S')
    line.append(usuario_global.fecha)
    line.append(usuario_global.hora)
    print(line)
    #print(line[0], line[1], line[3])
    #####################
    f = open("log.csv", "a")
    writer = csv.writer(f, delimiter=",")
    writer.writerow(line)
    f.close()

def logear(usuario_logeado):
    usuario_global.nombre = usuario_logeado
    usuario_global.accion = 'LOGIN'
    graba_log()
    #####################

def DecoradorLoggeo(funcion):
    def envoltura(*args, **kwargs):
        #global numero_de_llamada
        #numero_de_llamada += 1
        print('\nnombre de la función con el que entra al decorador: {}\n'.format(funcion.__name__.upper()))
        usuario_global.accion = funcion.__name__.upper()
        if funcion.__name__ == 'alta':
            ##### cantidad de registros actuales en la base de datos + el nuevo #####
            usuario_global.id_afectado = Students.select().count() + 1 
            print('dni:{} name: {} {}'.format(args[1], args[3], args[4]))
            # ojo que estos índices no coinciden en los parámetros que reciben las funciones modificacion y baja
        else:
            # elif funcion.__name__ == 'baja' or funcion.__name__ == 'modificacion':
            usuario_global.id_afectado = args[1]

# alta(self, dni, class_division, first_name, last_name, day_birth, status, sexo, address, line_phone, movile_phone1, movile_phone2):
        # if args:
        #     print('----Argumentos (números "*args" recibidos) de la función----')
        #     for i in args:
        #         print(i)
        # if kwargs:
        #     print('----Argumentos (números "**kwargs" recibidos) de la función----')
        #     for clave, valor in kwargs.items():
        #         print("%s == %s" % (clave, valor))
        graba_log()
        #####################
        return funcion(*args, **kwargs)
    return envoltura

##################################################################################################

class Alumnos:

    def recupera_alumnnos(self, tabla_recibida):
        # Consiguiendo datos
        contador = 0
        for row in Students.select():
            contador += 1
            print('fila {} campo dni: {} campo first_name {} '.format(contador, row.dni, row.first_name))
            #tabla_recibida.insert('',text=str(row[0]).zfill(5), values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
            tabla_recibida.insert("", END ,text=row.id, values=(row.dni, row.class_division, row.first_name, row.last_name, row.day_birth, row.status, row.sexo, row.address, row.line_phone, row.movile_phone1, row.movile_phone2))
    
    ##################################################################################################
    # def buscar_alumno_x_nombre(self, last_name):
    #     cur = self.cnn.cursor()
    #     linea_sql= "SELECT * FROM students WHERE last_name = '{}'".format(last_name)
    #     cur.execute(linea_sql)
    #     datos = cur.fetchone()
    #     cur.close()    
    #     return datos

    ##################################################################################################
    # def busca_alumno_x_dni(self, dni):
    #     cur = self.cnn.cursor()
    #     cur.execute("SELECT * FROM students WHERE dni = '{}'".format(dni))
    #     datos = cur.fetchall()
    #     for fila in datos:
    #         print(fila)
    #     cur.close()
    ##################################################################################################
       
    @DecoradorLoggeo
    def alta(self, dni, class_division, first_name, last_name, day_birth, status, sexo, address, line_phone, movile_phone1, movile_phone2):
        
        # datos = (dni.get(), class_division.get(), first_name.get(), last_name.get(), day_birth.get(),
        #      status.get(), sexo.get(), address.get(), line_phone.get(), movile_phone1.get(), movile_phone2.get())

        nueva_instancia = Students()
        nueva_instancia.dni = dni
        nueva_instancia.class_division = class_division
        nueva_instancia.first_name = first_name
        nueva_instancia.last_name = last_name
        nueva_instancia.day_birth = day_birth
        nueva_instancia.status = status
        nueva_instancia.sexo = sexo
        nueva_instancia.address = address
        nueva_instancia.line_phone = line_phone
        nueva_instancia.movile_phone1 = movile_phone1
        nueva_instancia.movile_phone2 = movile_phone2
        nueva_instancia.save()

    @DecoradorLoggeo
    def baja(self,register):

        borra = Students.get(Students.id == register)
        print('valor de borra: ')
        print(borra)
        print(type(borra))
        borra.delete_instance()

    @DecoradorLoggeo
    def modificacion(self, id, get_dni, get_class_division, get_first_name, get_last_name, get_day_birth, get_status, get_sexo, get_address, get_line_phone, get_movile_phone1, get_movile_phone2):
        
        register = id # --> class 'int'
        actualiza = Students.update(dni=get_dni, class_division=get_class_division, first_name=get_first_name, last_name=get_last_name, day_birth=get_day_birth, status=get_status, sexo=get_sexo, address=get_address, line_phone=get_line_phone, movile_phone1=get_movile_phone1, movile_phone2=get_movile_phone2).where(Students.id==register)
        actualiza.execute()


