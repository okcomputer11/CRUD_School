from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as MessageBox

from login_3_modell_mysql import *

root = Tk()

nombre_ingresado = StringVar()
contra_ingresado = StringVar()

usuario = User_actual()

def createGUI():
    # ventana principal
    #root = Tk()
    root.title("Login Usuario")

    # mainFrame
    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width=480,height=320)#,bg="lightblue")

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
    iniciarSesionButton = ttk.Button(mainFrame,text="Iniciar Sesion",command=iniciarSesion)
    iniciarSesionButton.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    # cerrarSesionButton = ttk.Button(mainFrame,text="Cerrar Sesion",command=cerrarSesion)
    btn_mensaje = ttk.Button(mainFrame,text="Olvidó usuario y/o contraseña",command=mensaje_olvido)
    btn_mensaje.grid(column=0,row=3)

    root.mainloop()

def mensaje_olvido():
    MessageBox.showerror("Error","contactese con el administrador del sistema")

def iniciarSesion():
    if usuario.intentos > 0:
        usuario.name = nombre_ingresado.get()
        usuario.password = contra_ingresado.get()
        ##################################
        coincidencia = usuario.verificar()
        ##################################
        usuario.intentos -= 1
        if coincidencia:
            MessageBox.showinfo(title='Login', message='\n       Bienvenida/o {}\n\nse ha logeado exitosamente'.format(usuario.name.upper()))
            # pasarle a la ventana principal los datos del usuario
            root.destroy()
        else:
            if usuario.intentos > 0:
                MessageBox.showwarning(title='NOMBRE O PASSWORD INCORRECTO', message='Le quedan {} intentos'.format(usuario.intentos))
            else:
                MessageBox.showerror("5 intentos fallidos","contactese con el administrador del sistema")
                root.destroy()

if __name__=="__main__":
    createGUI()