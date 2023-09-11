from tkinter import *
from tkinter import ttk
from typing import ItemsView
from alumnos_ORM import *
from tkinter import messagebox
#from log.login_window import *

alto_total = 650
largo_total= 1200

class Ventana_root(Frame):

    estudiantes = Alumnos()

    def __init__(self, master=None):
        super().__init__(master,width=largo_total, height=alto_total)

        self.master = master
        self.pack()
        
        self.crear_widgets()
        self.actualizaTreeView()
        self.habilita_cajas('disabled')
        self.habilita_botones_edicion('disabled')
        self.register = -1 #para saber si estoy creando nuevo o modificando un registro ya existente

    def actualizaTreeView(self):
                                    # para que esto funcione con "alumnos.py" sin ORM:
                                    # habilitar la sig. llamada a la función (en lugar de la que está ahora)
                                    # todo = self.estudiantes.recupera_alumnnos()
                                    # ( todo es type --> list )
        self.estudiantes.recupera_alumnnos(self.tabla)
                                    # y habilitar las líneas del ciclo for
        # for fila in todo:
        #     print(fila[0],fila[1],fila[4]) # imprime esas columnas de cada fila
        #     print(fila) # imprime la fila completa
        #     r=fila[0] # la columna 0, o sea, Id o nro. de registro
        #     self.tabla.insert('',END,text=str(r).zfill(5), values=(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11]))

        print(self.tabla.get_children())
        cant=str(len(self.tabla.get_children()))
        print(cant)
        self.etiqueta_cant_elementos.config(text="cantidad de registros: " + cant)

    def habilita_cajas(self,estado):
        self.caja_dni.configure(state=estado)
        self.caja_class.configure(state=estado)
        self.caja_fn.configure(state=estado)
        self.caja_ln.configure(state=estado)
        self.caja_birthday.configure(state=estado)
        self.caja_status.configure(state=estado)
        self.caja_sex.configure(state=estado)
        self.caja_address.configure(state=estado)
        self.caja_lphone.configure(state=estado)
        self.caja_mphone1.configure(state=estado)
        self.caja_mphone2.configure(state=estado)

    def limpia_cajas(self):
        self.caja_dni.delete(0,END)
        self.caja_class.delete(0,END)
        self.caja_fn.delete(0,END)
        self.caja_ln.delete(0,END)
        self.caja_birthday.delete(0,END)
        self.caja_status.delete(0,END)
        self.caja_sex.delete(0,END)
        self.caja_address.delete(0,END)
        self.caja_lphone.delete(0,END)
        self.caja_mphone1.delete(0,END)
        self.caja_mphone2.delete(0,END)

    def limpiaTreeview(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

    def fNuevo(self):        
        self.habilita_cajas('normal')
        self.limpia_cajas()
        self.caja_dni.focus()
        self.habilita_botones_laterales('disabled')
        self.habilita_botones_edicion('normal')
    
    def habilita_botones_laterales(self,estado):
        self.btn_nuevo.configure(state=estado)
        self.btn_modificar.configure(state=estado)
        self.btn_eliminar.configure(state=estado)
        self.btn_salir.configure(state=estado)

    def habilita_botones_edicion(self,estado):
        self.btn_guardar.configure(state=estado)
        self.btn_cancelar.configure(state=estado)
        
    def fGuardar(self):   
        if self.register == -1:   
            # Alta o Nuevo #
            self.estudiantes.inserta_alumno(self.caja_dni.get(), self.caja_class.get(), self.caja_fn.get(), self.caja_ln.get(), self.caja_birthday.get(), self.caja_status.get(), self.caja_sex.get(), self.caja_address.get(), self.caja_lphone.get(), self.caja_mphone1.get(), self.caja_mphone2.get())
            messagebox.showinfo("Nuevo Elemento", 'Elemento creado correctamente.')
        else:
            # Modificacion #
            self.estudiantes.modifica_alumno(self.register, self.caja_dni.get(), self.caja_class.get(), self.caja_fn.get(), self.caja_ln.get(), self.caja_birthday.get(), self.caja_status.get(), self.caja_sex.get(), self.caja_address.get(), self.caja_lphone.get(), self.caja_mphone1.get(), self.caja_mphone2.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.register = -1 # y acá le vuelvo a asignar el valor por defecto

        self.limpiaTreeview()
        self.actualizaTreeView()            
        self.limpia_cajas()
        self.habilita_cajas('disabled')
        self.habilita_botones_edicion('disabled')
        self.habilita_botones_laterales('normal')

    def fModificar(self):     
        item_seleccionado = self.tabla.focus()
        clave = self.tabla.item(item_seleccionado,'text') # devuelve SOLO el id (nro. de registro)
        if clave=='':
            messagebox.showwarning(title='Modificar', message='Debe seleccionar un registro')
        else:
            self.limpia_cajas()
            self.habilita_cajas('normal')
            self.habilita_botones_laterales('disabled')
            self.habilita_botones_edicion('normal')
            self.caja_dni.focus() # coloca el cursor en la caja con el "dni"

            valores = self.tabla.item(item_seleccionado,'values') # devuelve solo las columnas y sin el id (nro. registro)

            self.register = clave ############# para enviarlo con "estudiantes.modifica_alumno" en fGuardar

            self.caja_dni.insert(0,valores[0])
            self.caja_class.insert(0,valores[1])
            self.caja_fn.insert(0,valores[2])
            self.caja_ln.insert(0,valores[3])
            self.caja_birthday.insert(0,valores[4])
            self.caja_status.insert(0,valores[5])
            self.caja_sex.insert(0,valores[6])
            self.caja_address.insert(0,valores[7])
            self.caja_lphone.insert(0,valores[8])
            self.caja_mphone1.insert(0,valores[9])
            self.caja_mphone2.insert(0,valores[10])

    def fEliminar(self):
        item_seleccionado = self.tabla.focus()
        #fila_seleccionada = self.tabla.item(item_seleccionado) # devuelve TODOS los datos de una fila
        valores = self.tabla.item(item_seleccionado,'values') # devuelve solo las columnas y sin el id(nro. registro)
        clave = self.tabla.item(item_seleccionado,'text') # devuelve SOLO el id(nro. de registro)

        if clave=='':
            messagebox.showwarning(title='Alerta', message='Debe seleccionar un alumno')
        else:
            dato_persona = valores[2] + ' ' + valores[3] + ' dni: ' + valores[0] + ', reg: ' + str(clave).zfill(5)
            resp = messagebox.askquestion(title='Alerta', message='¿Desea eliminar el registro de ' + dato_persona +'?')
            #r =messagebox.askquestion(title='Confirmacion', message='¿Esta seguro?')
            if resp == messagebox.YES:
                error = self.estudiantes.elimina_alumno(clave)
                if error == 1:
                    messagebox.showinfo(title='Eliminar', message='Elemento eliminado correctamente')
                    self.limpiaTreeview()
                    self.actualizaTreeView()
                else:
                    messagebox.showinfo(title='Eliminar', message='OCURRIO UN ERROR AL INTENTAR ELIMINAR')


    def fCancelar(self):
        resp = messagebox.askquestion(title='Confirmación', message='¿está seguro que desea cancelar la edición?')
        if resp == messagebox.YES:
            self.limpia_cajas()
            self.habilita_cajas('disabled')
            self.habilita_botones_edicion('disabled')
            self.habilita_botones_laterales('normal')
   

    def crear_widgets(self):
        
        hi_li_ba_1 = "purple" # highlightbackground
        hi_li_ba_2 = "violet"
        fore_1 = "teal" # "cyan"
        fore_2 = "blue"
        bg_cour1 = "#bfdaff"
        hi_li_ba_exit_color = "red"
        fore_exit_color = "black" # "lavender"
        # Additionally, tkinter also supports specifying colors using hexadecimal color
        # codes, such as "#FF0000" for red or "#00FF00" for green.

        largo_frame1 = 95
        frame1 = Frame(self, bg=bg_cour1)
        frame1.place(x=0,y=0,width=largo_frame1, height=alto_total)  

        ##### Botones Laterales #####
        self.btn_nuevo=Button(frame1,text="Nuevo", command=self.fNuevo, highlightbackground=hi_li_ba_1, fg=fore_1)
        self.btn_nuevo.place(x=5,y=50,width=80, height=30 )        
        
        self.btn_modificar=Button(frame1,text="Modificar", command=self.fModificar,
                                   highlightbackground=hi_li_ba_1, fg=fore_1,
                                   activebackground=fore_2, activeforeground=fore_1,
                                   background=fore_2,foreground=fore_1)
        self.btn_modificar.place(x=5,y=100,width=80, height=30)                
        
        self.btn_eliminar=Button(frame1,text="Eliminar", command=self.fEliminar, highlightbackground=hi_li_ba_1, fg=fore_1)
        self.btn_eliminar.place(x=5,y=150,width=80, height=30)
        
        self.btn_salir=Button(frame1,text="Salir/Quit", command=self.master.destroy, highlightbackground=hi_li_ba_exit_color, fg=fore_exit_color)
        self.btn_salir.place(x=5,y=300,width=80, height=30)

        
        ###################################################### 
        """
        register (clave)
        dni (2da clave primaria)
        class_division
        first_name
        last_name
        day_birth
        status
        sexo
        address
        line_phone
        movile_phone1
        movile_phone2
        """
        largo_frame2 = 300
        ancho_entradas_largas = 280
        ancho_entradas_cortas = 40
        altura_entradas = 20
        separacion=8
        esp=20

        frame2 = Frame(self,bg=bg_cour1 ) # o highlightbackground
        frame2.place(x=100,y=0, width=largo_frame2, height=alto_total)                        
        
        eti1 = Label(frame2,text="dni: ")
        ly=separacion*3
        ly2=ly+esp
        eti1.place(x=3,y=ly)        
        self.caja_dni=Entry(frame2) 
        self.caja_dni.place(x=3,y=ly2,width=ancho_entradas_largas, height=altura_entradas)       
        
        eti2 = Label(frame2,text='class - division (ex. "1-1"): ')
        ly=separacion*9
        ly2=ly+esp
        eti2.place(x=3,y=ly)        
        self.caja_class=Entry(frame2)
        self.caja_class.place(x=3,y=ly2,width=ancho_entradas_cortas, height=altura_entradas)        
        
        eti3 = Label(frame2,text="First Name: ")
        ly=separacion*15
        ly2=ly+esp
        eti3.place(x=3,y=ly)        
        self.caja_fn=Entry(frame2)
        self.caja_fn.place(x=3,y=ly2,width=ancho_entradas_largas, height=altura_entradas) 

        eti4 = Label(frame2,text="Last Name: ")
        ly=separacion*21
        ly2=ly+esp
        eti4.place(x=3,y=ly)        
        self.caja_ln=Entry(frame2)
        self.caja_ln.place(x=3,y=ly2,width=ancho_entradas_largas, height=altura_entradas) 

        eti5 = Label(frame2,text="Day of Birth (ex. yyyy-mm-dd): ")
        ly=separacion*27
        ly2=ly+esp
        eti5.place(x=3,y=ly)        
        self.caja_birthday=Entry(frame2)
        self.caja_birthday.place(x=3,y=ly2,width=ancho_entradas_largas, height=altura_entradas) 

        eti6 = Label(frame2,text="Status (R= Regular L=Libre E=Egresado): ")
        ly=separacion*33
        ly2=ly+esp
        eti6.place(x=3,y=ly)        
        self.caja_status=Entry(frame2)
        self.caja_status.place(x=3,y=ly2,width=ancho_entradas_cortas, height=altura_entradas) 

        eti7 = Label(frame2,text="Sex (M/F/D): ")
        ly=separacion*39
        ly2=ly+esp
        eti7.place(x=3,y=ly)        
        self.caja_sex=Entry(frame2)
        self.caja_sex.place(x=3,y=ly2,width=ancho_entradas_cortas, height=altura_entradas) 

        eti8 = Label(frame2,text="Address: ")
        ly=separacion*45
        ly2=ly+esp
        eti8.place(x=3,y=ly)        
        self.caja_address=Entry(frame2)
        self.caja_address.place(x=3,y=ly2,width=ancho_entradas_largas, height=altura_entradas) 

        eti9 = Label(frame2,text="Phone: ")
        ly=separacion*51
        ly2=ly+esp
        eti9.place(x=3,y=ly)        
        self.caja_lphone=Entry(frame2)
        self.caja_lphone.place(x=3,y=ly2,width=ancho_entradas_largas, height=altura_entradas) 

        eti10 = Label(frame2,text="movile phone 1: ")
        ly=separacion*57
        ly2=ly+esp
        eti10.place(x=3,y=ly)        
        self.caja_mphone1=Entry(frame2)
        self.caja_mphone1.place(x=3,y=ly2,width=ancho_entradas_largas, height=altura_entradas)        
        
        eti11 = Label(frame2,text="movile phone 2: ")
        ly=separacion*63
        ly2=ly+esp
        eti11.place(x=3,y=ly)
        self.caja_mphone2=Entry(frame2)
        self.caja_mphone2.place(x=3,y=ly2,width=ancho_entradas_largas, height=altura_entradas)        

        ##### Botones Centrales #####

        self.btn_guardar=Button(frame2,text="Guardar", command=self.fGuardar, highlightbackground=hi_li_ba_1, fg=fore_1)
        self.btn_guardar.place(x=80,y=ly2+40,width=60, height=30)
        
        self.btn_cancelar=Button(frame2,text="Cancelar", command=self.fCancelar, highlightbackground=hi_li_ba_2, fg=fore_2)
        self.btn_cancelar.place(x=150,y=ly2+40,width=60, height=30)

        ######################################     

        posicion_frame3 = largo_frame1 + largo_frame2 + 4
        largo_frame3 = largo_total - (largo_frame1 + largo_frame2) - 10

        frame3 = Frame(self,background="brown")
        frame3.place(x=posicion_frame3, y=0, width=largo_frame3, height=alto_total-50)

        chico=30 
        medio=60
        largo=100                   
        
        self.tabla = ttk.Treeview(frame3, columns=("dni","class","fn","ln","birth","status","sex","address","lphone","cel1","cel2"))      
        self.tabla.column("#0",      width=medio)  # self.tabla.column("reg",width=chico,anchor=CENTER)
        self.tabla.column("dni",     width=largo, anchor=CENTER)
        self.tabla.column("class",   width=chico, anchor=CENTER)
        self.tabla.column("fn",      width=largo, anchor=W)
        self.tabla.column("ln",      width=largo, anchor=W)
        self.tabla.column("birth",   width=largo, anchor=CENTER)        
        self.tabla.column("status",  width=chico, anchor=CENTER)
        self.tabla.column("sex",     width=chico, anchor=CENTER)
        self.tabla.column("address", width=largo, anchor=W)
        self.tabla.column("lphone",  width=largo, anchor=W)
        self.tabla.column("cel1",    width=largo, anchor=W)
        self.tabla.column("cel2",    width=largo, anchor=W)

        self.tabla.heading("#0",     text="reg", anchor=CENTER) #self.tabla.heading("reg",text="reg",anchor=CENTER)
        self.tabla.heading("dni",    text="dni", anchor=CENTER)
        self.tabla.heading("class",  text="class", anchor=CENTER)
        self.tabla.heading("fn",     text="first name", anchor=CENTER)
        self.tabla.heading("ln",     text="last name", anchor=CENTER)
        self.tabla.heading("birth",  text="birthday", anchor=CENTER)
        self.tabla.heading("status", text="status", anchor=CENTER)
        self.tabla.heading("sex",    text="sex", anchor=CENTER)
        self.tabla.heading("address",text="address", anchor=CENTER)
        self.tabla.heading("lphone", text="line phone", anchor=CENTER)
        self.tabla.heading("cel1",   text="movile phone 1", anchor=CENTER)
        self.tabla.heading("cel2",   text="movile phone 2", anchor=CENTER)

        #self.tabla.pack(side=TOP, fill=NONE)
        self.tabla.place(x=20,y=10,width=largo_frame3-57, height=alto_total-105)

        barra_horizontal = Scrollbar(frame3, orient=HORIZONTAL)
        barra_horizontal.pack(side=BOTTOM, fill=X)
        self.tabla.config(xscrollcommand=barra_horizontal.set)
        barra_horizontal.config(command=self.tabla.xview)

        barra_vertical = Scrollbar(frame3, orient=VERTICAL)
        barra_vertical.pack(side=RIGHT, fill=Y)
        self.tabla.config(yscrollcommand=barra_vertical.set)
        barra_vertical.config(command=self.tabla.yview)

        self.tabla['selectmode']='browse' # permite seleccionar sólo 1 elemento (fila) por vez, aunque se presione SHIFT
        
        self.etiqueta_cant_elementos = Label(frame3,width=24,text="cantidad de registros: ")
        self.etiqueta_cant_elementos.place(x=largo_frame3-260, y=alto_total-92)

