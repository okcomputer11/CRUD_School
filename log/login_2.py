from tkinter import *
from modelo_base_users import *


class User_actual:
    def __init__(self, nombre='', clave=''):

        self.name = nombre
        self.password = clave
        self.conected = False
        self.intentos = 5

    def __str__(self):
        if self.conected:
            conect = "conectado"
        else:
            conect = "desconectado"
        return f"El nombre de usuario es {self.name} y estoy {conect}"

    def logear(self): # funciona, a la clasica
        erfolg = False
        while (self.intentos > 0) and (not erfolg):
            self.name = input("Ingrese un nombre: ")
            self.password = input("Igrese una contraseña: ")
            erfolg = self.verificar()
            self.intentos-=1
        if not erfolg:
            print("Error, no se pudo iniciar sesion.")
            print("Adios!!")

    def logear2(self): ########## funciona, con recursividad
        self.name = input("Ingrese un nombre: ")
        self.password = input("Igrese una contraseña: ")
        self.intentos-=1
        erfolg = self.verificar()
        if not erfolg:
            if self.intentos > 0:
                self.logear2()
            else:
                print("Error, no se pudo iniciar sesion.")
                print("Adios!!")

    def verificar(self):
        # corroborar si el usuario existe: if self.nombre == nombre en database
        # si existe,
            # comparar la contraseña ingresada (self.contra) con la que está almacenada en disco
            # si coinciden
                # hacer login
            # si no
                # mostrar: nombre o contraseña incorrecta
                # mostrar quedan tantos intentos y volver a permitir el ingreso de self.nombre y self.password
        if self.comprobacion(): #self.name, self.password):
            print('*'*40)
            print("****   Se ha conectado con exito!!  ****")
            self.conected = True
            print('*'*40)
            return True
        else:
            print('nombre o contraseña incorrecta')
            return False

    def desconectar(self):
        print('-'*100)
        if self.conected:
            print("Se cerro sesion con exito!!")
            self.conected = False
        else:
            print("Error, aún no inició sesion")
        print('-'*100)


    def comprobacion(self, ): # usuario, contra):
        #print('nombre y contraseña ingresada: {} \ {}'.format(usuario.get(), contra.get()))
        print('Se han ingresado --> nombre: {} y --> contraseña: {}'.format(self.name, self.password))
        #print('usuarios existentes')
        #contador = 0
        #for fila in Users.select(): # busca en la base de datos
            #contador += 1
        #    print(fila.id, fila.nombre, fila.password)
        pass_guardado = ''
        if self.name == 'juan':
            pass_guardado = '1234'
        #else:
        #    print('ERROR... el usuario no existe')
    
        ################### acá busca e la Base de Datos el usuario y si existe devuelve su conraseña almacenada
        #try:
        #    pass_guardado = Users.get(Users.name == usuario.get()).password # así busca por nonmbre y devuelve el password
        #except:
        #    print('ERROR... el usuario no existe')
        #    pass_guardado = ''

        if pass_guardado  != '': # el usuario existe
            #print('contraseña almacenada del usuario {}: {}'.format(usuario.get(), query))
            print('contraseña almacenada del usuario {}: {}'.format(self.name, pass_guardado))
            #if pass_guardado == contra.get():
            if pass_guardado == self.password:
                return True # si coincide usuario con contraseña
            else:
                return False
    
if __name__ == "__main__":
    
    user1 = User_actual()
    print(user1)

    user1.logear() # o logear2, son iguales
    print(user1)

    user1.desconectar()
    print(user1)

"""   

class Ventana_log:

    def __init__(self, window):
        
        ############################################################
        self.objeto_base = Verificacion()  #  en modelo_base_users
        ############################################################

        self.ventana_login = window
        
        self.ventana_login.wm_title("Login 1")
        self.ventana_login.title("Login 2")

        # Frame
        self.ventana_login.geometry("290x110")
        self.ventana_login.resizable(0,0) # no se puede modificar ni de ancho ni de alto
        self.ventana_login.grid() #row=10, column=0, columnspan=4)

        # Etiquetas
        self.superior = Label(self.ventana_login, text="Ingrese sus datos", bg="orchid", fg="white", width=18)
        self.superior.grid(row=0, column=1, columnspan=1, padx=0, pady=1, sticky="w" ) #"w" + "e")
     
        self.eti_nombre = Label(self.ventana_login, text="nombre de usuario")
        self.eti_nombre.grid(row=1, column=0, sticky="n")

        self.eti_password = Label(self.ventana_login, text="contraseña")
        self.eti_password.grid(row=2, column=0, sticky="n")

        # Entradas
        self.caja_nombre = Entry(self.ventana_login, textvariable=self.user)
        self.caja_nombre.grid(row=1, column=1)

        self.caja_password = Entry(self.ventana_login, textvariable=self.password, show='*')
        self.caja_password.grid(row=2, column=1)
     
        # Boton
        self.boton_ok = Button(self.ventana_login, text="iniciar sesión", fg="red",bg="blue", command=lambda: self.verificar())
        self.boton_ok.grid(row=6, column=1)
    
    def verificar(self,):
        ok = self.objeto_base.comprobacion(self.user, self.password)
        if ok:
            print('BIENVENIDO {}'.format(self.user.get()))
            # le tengo que devolver el nombre de usuario -> self.user.get() a la ventana principal
            # y esta ventana se tiene que destruir
            self.ventana_login.destroy()

        else:
            print('usuario y/o contraseña incorrecta... vuelvalo a intentar')


#####################################################################################################
############# supongo que de aquí para abajo debe anularse todo, cuando exista una ventana principal

# class Controller:

#     def __init__(self, root):
#         print('-'*100)
#         self.root_controler = root
#         Ventana_log(self.root_controler)

# if __name__ == "__main__":
#     root_tk = Tk()
#     application = Controller(root_tk)
#     root_tk.mainloop()

"""