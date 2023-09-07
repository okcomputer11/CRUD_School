from ventana import *
import tkinter as tk

def main():
    root = tk.Tk()
    root.title('CRUD Alumnos Escuela x') # root.wm_title("CRUD Python con MySQL") 
    root.resizable(0,0) # no se puede modificar ni de ancho ni de alto
    app = Ventana_root(root) 
    app.mainloop()

if __name__ == '__main__':
    main()
