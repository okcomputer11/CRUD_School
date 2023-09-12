from tkinter import *
from tkinter import messagebox as MessageBox
from ventana_con_login import *
from log.login_3_modell_mysql import *

# pip install pymysql


#############################################################################################################
# main_con_login.py     --> modulo (actual) principal
#                           Contiene la gráfica del login (nombre y contraseña del usuario)
#
# log/login_3_modell_mysql  -->  *) En este modulo se encarga de hacer la parte lógica del Login
#                                   o sea, comprobar que la persona que va a operar en el sistema
#                                   tiene nombre y contraseña en la base de datos mysql:
#                                   host="localhost", user="root", passwd="sofocles11", database="escuela"
#                                *) Aquí está definida la clase User_actual()
#                                                                             self.name
#                                                                             self.password
#                                                                             self.conected
#                                                                             self.intentos
#
# ........... si el usuario ingresa correctamente nombre y contraseña, continúa con los sig. módulos ...........
#
# ventana_con_login     --> modulo gráfico (tkinter)
#                           dentro está definida la clase Ventana_root() que contiene toda la grafica
#
# alumnos_ORM           --> *) Acá trabaja con la base de datos de los alumnos: db = SqliteDatabase('Schule.db')
#                               definida en la clase Students()
#                           *) También tiene una clase Loggeo() para almacenar los datos del usuario (o dataentry)
#                               Con estos datos se lleva a cabo un log en el archivo "log.csv",
#                               cada vez que el usuario mofifica algo (o cuando se logea)
#
#############################################################################################################

def createGUI():

    ventanaLog = Tk()

    nombre_ingresado = StringVar()
    contra_ingresado = StringVar()

    # ventana principal
    ventanaLog.title("Login Usuario")

    # mainFrame
    mainFrame = Frame(ventanaLog)
    mainFrame.pack()
    #mainFrame.config(width=480,height=320)#,bg="lightblue")

    # textos y titulos
    titulo = Label(mainFrame,text="Ingrese sus datos para trabajar",font=("Arial",24))
    titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)

    nombreLabel = Label(mainFrame,text="Nombre: ")
    nombreLabel.grid(column=0,row=1)
    passLabel = Label(mainFrame,text="Contraseña: ")
    passLabel.grid(column=0,row=2)

    # entradas de texto
    # nombreUsuario = StringVar()
    nombre_ingresado.set("")
    nombreEntry = Entry(mainFrame,textvariable=nombre_ingresado)
    nombreEntry.grid(column=1,row=1)

    # contraUsuario = StringVar()
    contra_ingresado.set("")
    contraEntry = Entry(mainFrame,textvariable=contra_ingresado,show="*")
    contraEntry.grid(column=1,row=2)

    # botones
    iniciarSesionButton = ttk.Button(mainFrame,text="Iniciar Sesion",command=lambda:iniciarSesion(ventanaLog, nombre_ingresado, contra_ingresado))
    iniciarSesionButton.grid(column=0,row=3,ipadx=5,ipady=5,padx=10,pady=10)

   # exitButton = ttk.Button(mainFrame,text="Cerrar Sesion",command=cerrarSesion)
    btn_exit = ttk.Button(mainFrame,text="Exit",command=hacer_exit)
    btn_exit.grid(column=1,row=3)

    # cerrarSesionButton = ttk.Button(mainFrame,text="Cerrar Sesion",command=cerrarSesion)
    btn_mensaje = ttk.Button(mainFrame,text="Olvidó usuario y/o contraseña",command=mensaje_olvido)
    btn_mensaje.grid(column=1,row=4)

    ventanaLog.mainloop()

def hacer_exit():
    raise SystemExit(0)

def mensaje_olvido():
    MessageBox.showerror("Error","contactese con el administrador del sistema")

def iniciarSesion(ventana, name_ingresado, pass_ingresado):

    # MySql database --> "db_usuarios_old" --> table Users #
    
    if usuario.intentos > 0:
        usuario.name = name_ingresado.get()
        usuario.password = pass_ingresado.get()
        ##################################
        coincidencia = usuario.verificar()
        ##################################
        usuario.intentos -= 1
        if coincidencia:
            MessageBox.showinfo(title='Login', message='\n       Bienvenida/o {}\n\nse ha logeado exitosamente'.format(usuario.name.upper()))
            usuario.conected = True
            # pasarle a la ventana principal los datos del usuario
            ventana.destroy()
        else:
            if usuario.intentos > 0:
                MessageBox.showwarning(title='NOMBRE O PASSWORD INCORRECTO', message='Le quedan {} intentos'.format(usuario.intentos))
            else:
                MessageBox.showerror("3 intentos fallidos","contactese con el administrador del sistema")
                ventana.destroy()


if __name__=="__main__":

    usuario = User_actual() # definde in log/login_3_modell_mysql 

    #usuario.conected = True

    createGUI()

    #print('#'*100)

    if usuario.conected:
        ########################## le paso los datos del usuario logueado
        # instancia: usuario = User_actual()

        principal = Tk()
        principal.title('CRUD Alumnos Escuela x') # root.wm_title("CRUD Python con MySQL") 
        principal.resizable(0,0) # no se puede modificar ni de ancho ni de alto
        
        #app = Ventana_root(principal, usuario) 
        Ventana_root(principal, usuario) 
        #app.mainloop()
        principal.mainloop()
