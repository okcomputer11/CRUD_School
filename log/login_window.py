from tkinter import *
from modelo_base_users import *

class Ventana_log:

    def __init__(self, window):
        
        ############################################################
        self.objeto_base = Verificacion()  #  en modelo_base_users
        ############################################################

        #self.ventana_login = Toplevel(width=300, height=300)
        ############# la línea superior quizás para trabajarla en conexión con otra ventana principal
        self.ventana_login = window
        
        self.ventana_login.wm_title("Login 1")
        self.ventana_login.title("Login 2")

        self.user = StringVar()
        self.password = StringVar()
        
        # Frame
        self.ventana_login.geometry("290x110")
        self.ventana_login.resizable(0,0) # no se puede modificar ni de ancho ni de alto
        self.ventana_login.grid() #row=10, column=0, columnspan=4)

        # Etiquetas
        self.superior = Label(self.ventana_login, text="Ingrese sus datos", bg="orchid", fg="white", width=32)
        self.superior.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky="w" ) #"w" + "e")
     
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

class Controller:

    def __init__(self, root):
        print('-'*100)
        self.root_controler = root
        Ventana_log(self.root_controler)

if __name__ == "__main__":
    root_tk = Tk()
    application = Controller(root_tk)
    root_tk.mainloop()