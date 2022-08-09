from tkinter import *
from tkinter.messagebox import *
import sqlite3
import tkinter as tk
import time
from tkinter import ttk
from tkinter import messagebox
        
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
  


def ir_home():
    pass
def registrar():
    ventana = Toplevel(root)
    ventana.title("Registro De Usuario")
    ventana.iconbitmap("graficos/logo.ico")
    ventana.geometry("346x402+380+50")
    ventana.resizable(width=False, height=False)
    ventana.transient(root)

    tapiz = PhotoImage(file="graficos/tapiz_registrar.png")
    Label(ventana, image=tapiz).place(x=0, y=0, relwidth=1, relheight=1)

    def agregar():
        
        conex = sqlite3.connect("base.db")

        cursor = conex.cursor()

        usua = usuario.get()
    
        contra = contrasena.get()
        contra2 = contrasena2.get()
    
    
        if(contra==contra2 and usua!='' and contra!=''):
                try:
                    cursor.execute("INSERT INTO login VALUES(\'"+usua+"\',\'"+contra+"')")
                    showinfo(title="Eso es",message="¡Felicidades!, registro exitoso")
                    conex.commit()
                    conex.close()
                    ventana.destroy()
                    
                    
                except sqlite3.Error as er:
                    showerror(title="Ups, algo salio mal", message="¡Este usuario ya fue creado!")
                    ventana.destroy()
                    conex.close()
                    
    
        elif(contra!=contra2):
            showerror(title="Ups, algo salio mal", message="¡Las contraseñas no coinciden!")
            ventana.destroy()

        elif(usua=='' or contra==''):
            showerror(title="Ups, algo salio mal", message="¡Coloque un usuario y una contraseña!")
            
    
    def on_write(*args):
        s = var.get()
        if len(s) > 0: 
            var.set(s[:max_len])
        
    def on_write2(*args):
        s2 = var2.get()
        if len(s2) > 0: 
            var2.set(s2[:max_len2])
        
    def on_write3(*args):
        s3 = var3.get()
        if len(s3) > 0: 
            var3.set(s3[:max_len3])
        
    max_len = 15
    var = StringVar()
    var.trace("w", on_write)

    max_len2 = 10
    var2 = StringVar()
    var2.trace("w", on_write2)

    max_len3 = 10
    var3 = StringVar()
    var3.trace("w", on_write3)

    usuario = Entry(ventana,bg="#1b0117",textvariable=var,relief="flat",justify="center",font="ubuntu 14",fg="white",width=16)
    usuario.place(x=80, y=119)
    usuario.config(insertbackground="#fd6418")

         
    contrasena = Entry(ventana,width=16,bg="#1b0117",textvariable=var2,justify="center",relief="flat",font="ubuntu 14",fg="white", show="*")
    contrasena.place(x=80, y=171)
    contrasena.config(insertbackground="#fd6418")


    contrasena2 = Entry(ventana,width=16,textvariable=var3,justify="center",bg="#1b0117",relief="flat",font="ubuntu 14",fg="white", show="*")
    contrasena2.place(x=81, y=221)
    contrasena2.config(insertbackground="#fd6418")
  
    iniciar = Button(ventana,text="REGISTRAR",cursor="hand2",width=13,relief="flat",font="impact 14",bg="#fd6418", command=agregar)
    iniciar.place(x=110, y=295)
    iniciar.config(activebackground="#a65208", activeforeground="gray")
  
    ventana.mainloop()


def home():
    global root

    root = Tk()
    root.title("Gestor De Inventario")
    root.iconbitmap("graficos/logo.ico")
    root.geometry("1010x530+0+0")
    root.resizable(width=False, height=False)
    
    img_boton = PhotoImage(file="graficos/microbiologia.png",height=150,width=150)
    boton = Button(image=img_boton,cursor="hand2",relief="flat",bg="orange",fg="red", command=home1)
    boton.place(x=50, y=50)
    CreateToolTip(boton, text = 'Este boton te dirige\n'
                  'al inventario de Microbiologia')

    img_boton1 = PhotoImage(file="graficos/fisicoquimica.png",height=150,width=150)
    boton1 = Button(image=img_boton1,cursor="hand2",relief="flat",bg="orange",fg="red", command=home2)
    boton1.place(x=130, y=50)
    CreateToolTip(boton1, text = 'Este boton te dirige\n'
                  'al inventario de Fisicoquimica')


    img_boton2 = PhotoImage(file="graficos/bioinsumo.png",height=150,width=150)
    boton2 = Button(image=img_boton2,cursor="hand2",relief="flat",bg="blue",fg="red", command=home3)
    boton2.place(x=210, y=50)
    CreateToolTip(boton2, text = 'Este boton te dirige\n'
                  'al inventario de Bioinsumo')


    img_boton3 = PhotoImage(file="graficos/florayfauna.png",height=150,width=150)
    boton3 = Button(image=img_boton3,cursor="hand2",relief="flat",bg="blue",fg="red", command=home4)
    boton3.place(x=290, y=50)
    CreateToolTip(boton3, text = 'Este boton te dirige\n'
                  'al inventario de Flora y Fauna')



    root.mainloop()



def home1():
    microbiologia = Toplevel(root)
    microbiologia.title("AREA MICROBIOLOGIA")
    microbiologia.iconbitmap("graficos/logo.ico")
    microbiologia.geometry("1010x530+0+0")
    microbiologia.resizable(width=False, height=False)
    microbiologia.transient(root)
    
    tapiz = PhotoImage(file="graficos/interfaz.png")
    Label(microbiologia, image=tapiz).place(x=0, y=0, relwidth=1, relheight=1)

    
    vId=StringVar()
    vNombre=StringVar()
    vTipo=StringVar()
    vUmedida=StringVar()
    vCantidad=IntVar()
    vDescripcion=StringVar()
    vStockmin=IntVar()
    vStockmax=IntVar()
    vUbicacion=StringVar()
    vEtiquetacolor=StringVar()
    vEmpaque=StringVar()
    vCaracteristica=StringVar()
    vFechavencimiento=StringVar()
    vCategoriaseguridad=StringVar()
    vGarantia=StringVar()

    def conexionBBDD():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()

	    try:
		    miCursor.execute('''
			    CREATE TABLE microbiologia (
			    ID INTEGER PRIMARY KEY AUTOINCREMENT,
			    NOMBRE VARCHAR(50) NOT NULL,
			    TIPO VARCHAR(50) NOT NULL,
			    UNIDAD_DE_MEDIDA VARCHAR(50) NOT NULL,
			    CANTIDAD INTEGER NOT NULL,
			    DESCRIPCION VARCHAR(120) NOT NULL,
			    STOCKMIN INTEGER NOT NULL,
			    STOCKMAX INTEGER NOT NULL,
			    UBICACION VARCHAR(50) NOT NULL,
			    ETIQUETACOLOR VARCHAR(50),
			    EMPAQUE VARCHAR(50),
			    CARACTERISTICA VARCHAR(50),
			    FECHAVENCIMIENTO DATE,
			    CATEGORIASEGURIDAD VARCHAR(50),
			    GARANTIA VARCHAR(50))
			    ''')

		    messagebox.showinfo("CONEXION","Base de Datos Creada exitosamente")
	    except:
		    messagebox.showinfo("CONEXION", "Conexión exitosa con la base de datos")

    def eliminarBBDD():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    if messagebox.askyesno(message="¿Los Datos se perderan definitivamente, Desea continuar?", title="ADVERTENCIA"):
	       miCursor.execute("DROP TABLE microbiologia")
	    else:
		    pass
	    limpiarCampos()
	    mostrar()

    def salirAplicacion():
	    valor=messagebox.askquestion("Salir","¿Está seguro que desea salir de la Aplicación?")
	    if valor=="yes":
		    root.destroy()

    def limpiarCampos():
	    vId.set("")
	    vNombre.set("")
	    vTipo.set("")
	    vUmedida.set("")
	    vCantidad.set("")
	    vDescripcion.set("")
	    vStockmin.set("")
	    vStockmax.set("")
	    vUbicacion.set("")
	    vEtiquetacolor.set("")
	    vEmpaque.set("")
	    vCaracteristica.set("")
	    vFechavencimiento.set("")
	    vCategoriaseguridad.set("")
	    vGarantia.set("")

    def mensaje():
	    acerca='''
	    Gestor De Inventario
	    Area Ambiental SENA
	    Version 1.0
	    Tecnología Python Tkinter
	    '''
	    messagebox.showinfo(title="INFORMACION", message=acerca)

    ################################ Métodos CRUD ##############################
    def erroragregar():
        nom=vNombre.get()
        can=vCantidad.get()

        if(nom=='' and can==''):
            try:
                messagebox.showwarning("¡ups!","!No se pudo guardar! Algunos Campos son necesarios")
            except:
                pass
		
        
    def crear():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()

	    erroragregar()

	    nom=vNombre.get()
	    can=vCantidad.get()
    
            
	    if(nom!='' and can!=''):
	            try:
		            datos=vNombre.get(),vTipo.get(),vUmedida.get(),vCantidad.get(),vDescripcion.get(),vStockmin.get(),vStockmax.get(),vUbicacion.get(),vEtiquetacolor.get(),vEmpaque.get(),vCaracteristica.get(),vFechavencimiento.get(),vCategoriaseguridad.get(),vGarantia.get()
		            miCursor.execute("INSERT INTO microbiologia VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datos))
		            miConexion.commit()
	            except:
		            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con BBDD")
		            pass
	            limpiarCampos()
	            miConexion.close()
	            llamar()
                
    def mostrar1():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    registros=tree.get_children()
	    for elemento in registros:
		    tree.delete(elemento)

	    try:
		    miCursor.execute("SELECT * FROM microbiologia WHERE TIPO='Herramienta'")
		    for row in miCursor:
			    tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
	    except:
		    pass
    def mostrar2():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM microbiologia WHERE TIPO='Aseo'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass

    def mostrar3():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM microbiologia WHERE TIPO='Epp'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass



    def mostrar4():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM microbiologia WHERE TIPO='Producción'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass



    def mostrar5():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM microbiologia WHERE TIPO='S-Controladas'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass


    def mostrar6():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM microbiologia WHERE TIPO='S-Grupo E'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass


    def mostrar7():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM microbiologia WHERE TIPO='Otro'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass

    def mostrar():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM microbiologia")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass
    ################################## Tabla ################################
    seleccion=IntVar()		
    sel=seleccion.get()
    def llamar():
        if sel==1:
            mostrar1()
        elif sel==2:
            mostrar2()
        elif sel==3:
            mostrar3()
        elif sel==4:
            mostrar4()
        elif sel==5:
            mostrar5()
        elif sel==6:
            mostrar6()
        elif sel==7:
            mostrar7()
        elif sel==8:
            mostrar()

            
    		
    rb_frame= Frame(microbiologia,width=150, height=160)
    rb_frame.place(x=820, y=25)
    rb_frame.config(bg="#c0bebe")

    

    
    Radiobutton(rb_frame, 
                value=1,variable=seleccion,text="HERRAMIENTAS",cursor='hand2',bg="#c0bebe",command=mostrar1).place(x=0,y=0)
    Radiobutton(rb_frame,
                value=2,variable=seleccion,text="ASEO",cursor='hand2',bg="#c0bebe",command=mostrar2).place(x=0,y=20)
    Radiobutton(rb_frame, 
                value=3,variable=seleccion,text="EPP",cursor='hand2',bg="#c0bebe",command=mostrar3).place(x=0,y=40)
    Radiobutton(rb_frame, 
                value=4,variable=seleccion,text="PRODUCCIÓN",cursor='hand2',bg="#c0bebe",command=mostrar4).place(x=0,y=60)
    Radiobutton(rb_frame,
                value=5,variable=seleccion,text="S-CONTROLADAS",cursor='hand2',bg="#c0bebe", command=mostrar5).place(x=0,y=80)
    Radiobutton(rb_frame, 
                value=6,variable=seleccion,text="S-GRUPO E",cursor='hand2',bg="#c0bebe", command=mostrar6).place(x=0,y=100)
    Radiobutton(rb_frame, 
                value=7,variable=seleccion,text="OTROS",cursor='hand2',bg="#c0bebe", command=mostrar7).place(x=0,y=120)
    Radiobutton(rb_frame, 
                value=8,variable=seleccion,text="TODOS",cursor='hand2',bg="#c0bebe", command=mostrar).place(x=0,y=140)



    

		
    tree_frame = Frame(microbiologia)
    tree_frame.place(x=10,y=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    
    tree_scroll2 = Scrollbar(tree_frame,orient="horizontal")
    tree_scroll2.pack(side=BOTTOM,fill=X)

	
    tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,xscrollcommand=tree_scroll2.set,height=8, columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12','#13'))
    tree.pack()

    tree_scroll.config(command=tree.yview)
    tree_scroll2.config(command=tree.xview)



    tree.heading('#0', text="ID", anchor=CENTER)
    tree.column('#0',width=40,minwidth=60)
    tree.heading('#1', text="Nombre", anchor=CENTER)
    tree.column('#1', width=50,minwidth=100)
    tree.heading('#2', text="Tipo", anchor=CENTER)
    tree.column('#2', width=50,minwidth=100)
    tree.heading('#3', text="Unidad de Medida", anchor=CENTER)
    tree.column('#3', width=50,minwidth=110)
    tree.heading('#4', text="Cantidad", anchor=CENTER)
    tree.column('#4', width=50,minwidth=100)
    tree.heading('#5', text="Descripcion", anchor=CENTER)
    tree.column('#5', width=50,minwidth=100)
    tree.heading('#6', text="Stock minimo", anchor=CENTER)
    tree.column('#6', width=50,minwidth=100)
    tree.heading('#7', text="Stock maximo", anchor=CENTER)
    tree.column('#7', width=50,minwidth=100)
    tree.heading('#8', text="Ubicación", anchor=CENTER)
    tree.column('#8',width=50,minwidth=100)
    tree.heading('#9', text="Etiqueta de Color", anchor=CENTER)
    tree.column('#9', width=50,minwidth=100)
    tree.heading('#10', text="Empaque", anchor=CENTER)
    tree.column('#10', width=50,minwidth=100)
    tree.heading('#11', text="Estado Caracteristico", anchor=CENTER)
    tree.column('#11', width=50,minwidth=120)
    tree.heading('#12', text="Fecha de Vencimiento", anchor=CENTER)
    tree.column('#12', width=50,minwidth=130)
    tree.heading('#13', text="Categoria de Seguridad", anchor=CENTER)
    tree.column('#13', width=50,minwidth=135)
    tree.heading('#14', text="Garantia", anchor=CENTER)
    tree.column('#14', width=50,minwidth=100)


    def seleccionarUsandoClick(event):
	    item=tree.identify('item',event.x,event.y)
	    vId.set(tree.item(item,"text"))
	    vNombre.set(tree.item(item,"values")[0])
	    vTipo.set(tree.item(item,"values")[1])
	    vUmedida.set(tree.item(item,"values")[2])
	    vCantidad.set(tree.item(item,"values")[3])
	    vDescripcion.set(tree.item(item,"values")[4])
	    vStockmin.set(tree.item(item,"values")[5])
	    vStockmax.set(tree.item(item,"values")[6])
	    vUbicacion.set(tree.item(item,"values")[7])
	    vEtiquetacolor.set(tree.item(item,"values")[8])
	    vEmpaque.set(tree.item(item,"values")[9])
	    vCaracteristica.set(tree.item(item,"values")[10])
	    vFechavencimiento.set(tree.item(item,"values")[11])
	    vCategoriaseguridad.set(tree.item(item,"values")[12])
	    vGarantia.set(tree.item(item,"values")[13])

	
    tree.bind("<Double-1>", seleccionarUsandoClick)



    def actualizar():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    try:
		    datos=vNombre.get(),vTipo.get(),vUmedida.get(),vCantidad.get(),vDescripcion.get(),vStockmin.get(),vStockmax.get(),vUbicacion.get(),vEtiquetacolor.get(),vEmpaque.get(),vCaracteristica.get(),vFechavencimiento.get(),vCategoriaseguridad.get(),vGarantia.get()
		    miCursor.execute("UPDATE microbiologia SET NOMBRE=?, TIPO=?, UNIDAD_DE_MEDIDA=?, CANTIDAD=?, DESCRIPCION=?, STOCKMIN=?, STOCKMAX=?, UBICACION=?, ETIQUETACOLOR=?, EMPAQUE=?, CARACTERISTICA=?, FECHAVENCIMIENTO=?, CATEGORIASEGURIDAD=?, GARANTIA=? WHERE ID="+vId.get(), (datos))
		    miConexion.commit()
	    except:
		    messagebox.showwarning("ATENCIÓN","Seleccione un producto haciendo ¡Doble click!")
		    pass
	    limpiarCampos()
	    llamar()

    def borrar():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    try:
		    if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
			    miCursor.execute("DELETE FROM microbiologia WHERE ID="+vId.get())
			    miConexion.commit()
	    except:
		    messagebox.showwarning("ATENCIÓN","Seleccione un producto haciendo ¡Doble click!")
		    pass
	    limpiarCampos()
	    llamar()

    ###################### Colocar widgets en la VISTA ######################
    ########## Creando Los menus ###############
    menubar=Menu(microbiologia)
    menubasedat=Menu(menubar,tearoff=0)
    menubasedat.add_command(label="Crear/Conectar Base de Datos", command=conexionBBDD)
    menubasedat.add_command(label="Eliminar Base de Datos", command=eliminarBBDD)
    menubasedat.add_command(label="Salir", command=salirAplicacion)
    menubar.add_cascade(label="Inicio", menu=menubasedat)

    ayudamenu=Menu(menubar,tearoff=0)
    ayudamenu.add_command(label="Vaciar Campos", command=limpiarCampos)
    ayudamenu.add_command(label="Info", command=mensaje)
    menubar.add_cascade(label="Ayuda",menu=ayudamenu)

    loginmenu=Menu(menubar,tearoff=0)
    loginmenu.add_command(label="Registrar usuario", command=registrar)
    loginmenu.add_command(label="Ver usuarios", command=mensaje)
    loginmenu.add_command(label="Borrar usuarios", command=mensaje)
    menubar.add_cascade(label="Login",menu=loginmenu)

    ############## Creando etiquetas y cajas de texto ###########################
    
    c_estilos=ttk.Style()
    c_estilos.theme_use("clam")

    c_estilos.configure("TCombobox",
          background="#d6dce5",
          foreground="black",
          rowheight=25,
          fieldbackground="#d6dce5"            
          )
    c_estilos.map('TCombobox',
           background=[('selected','#d6dce5')])


    estilos = ttk.Style()

    estilos.theme_use("alt")

    estilos.configure("Treeview",
          background="#c0bebe",
          foreground="black",
          rowheight=21,
          fieldbackground="d6dce5"            
          )
    estilos.map('Treeview',
           background=[('selected','#fd6418')])
   

    
    e1=Entry(microbiologia, textvariable=vId)


    e2=Entry(microbiologia, textvariable=vNombre,bg="#d6dce5",relief="flat", width=16)
    e2.place(x=41,y=260)

    c1=ttk.Combobox(microbiologia,width=16,textvariable=vTipo,state="readonly",values=["Herramienta","Aseo","Epp","Producción","S-Controladas","S-Grupo E","Otro"])
    c1.place(x=205,y=260)
    
    c2=ttk.Combobox(microbiologia,width=16,textvariable=vUmedida,state="readonly",values=["Unidad","Kilogramos","C-cubicos","Centimetros","Litros"])
    c2.place(x=362,y=260)

    def valida_caracteres(action, char, text):
        if action != "1":
            return True
        return char in "0123456789." and len(text)< 7
    validatecommand = microbiologia.register(valida_caracteres)
    e5=Entry(microbiologia, validate="key",validatecommand=(validatecommand, "%d","%S","%s"), textvariable=vCantidad,bg="#d6dce5",relief="flat", width=7)
    e5.place(x=41,y=311)


    e6=Entry(microbiologia, textvariable=vDescripcion,bg="#d6dce5",relief="flat", width=16)
    e6.place(x=213,y=311)


    e7=Entry(microbiologia, validate="key",validatecommand=(validatecommand, "%d","%S","%s"),textvariable=vStockmin,bg="#d6dce5",relief="flat", width=11)
    e7.place(x=370,y=311)


    e8=Entry(microbiologia, validate="key",validatecommand=(validatecommand,"%d","%S","%s"),textvariable=vStockmax,bg="#d6dce5",relief="flat", width=12)
    e8.place(x=41,y=366)


    e9=Entry(microbiologia, textvariable=vUbicacion,bg="#d6dce5",relief="flat", width=16)
    e9.place(x=213,y=366)

    
    c3=ttk.Combobox(microbiologia,width=17,textvariable=vEtiquetacolor,state="readonly",values=["Rojo |","Rojo ||","Amarillo","Azul","Verde","No Aplica"])
    c3.place(x=360,y=366)
    CreateToolTip(c3, text = 'Rojo | -Muy Toxico\n'
                             'Rojo || -Toxico\n'
                             'Amarillo -Nocivo\n'
                             'Azul -Poco Peligroso\n'
                             'Verde -No ofrece peligro')

    e11=Entry(microbiologia, textvariable=vEmpaque,bg="#d6dce5",relief="flat", width=16)
    e11.place(x=41,y=420)


    e12=Entry(microbiologia, textvariable=vCaracteristica,bg="#d6dce5",relief="flat", width=16)
    e12.place(x=213,y=419)

    def valida_fecha(action, char, text):
        if action != "1":
            return True
        return char in "0123456789/" and len(text)< 10
    validatecommand = microbiologia.register(valida_fecha)
    e13=Entry(microbiologia,validate="key",validatecommand=(validatecommand, "%d","%S","%s"), textvariable=vFechavencimiento,bg="#d6dce5",relief="flat", width=19)
    e13.place(x=370,y=420)


    c4=ttk.Combobox(microbiologia,width=22,textvariable=vCategoriaseguridad,state="readonly",values=["Explosivas(EX)","Inflamables(IN)","Comburentes(CB)","Gas bajo presión(GZ)","Corrosivas(CR)","Toxic Aguda Cat-1(TO)","Toxic Aguda Cat-2(TO)","Toxic Aguda Cat-3(TO)","Toxic Aguda Cat-4(DA)","Mutageno(MU)","Dañ/med Ambiente(EN)","Ninguna"])
    c4.place(x=34,y=473)
    

    e15=Entry(microbiologia, textvariable=vGarantia,bg="#d6dce5",relief="flat", width=16)
    e15.place(x=213,y=473)



    ################# Creando botones ###########################

    b2=Button(microbiologia, text="Registrar",cursor="hand2",bg="#fd6418",relief="flat",width=12,font="ubuntu 10",fg="white", command=crear)
    b2.place(x=558,y=305)
    b2.config(activebackground="#a65208", activeforeground="gray")
    b3=Button(microbiologia, text="Modificar",cursor="hand2",bg="#fd6418",relief="flat",width=12,font="ubuntu 10",fg="white", command=actualizar)
    b3.place(x=558,y=363)
    b3.config(activebackground="#a65208", activeforeground="gray")
    b4=Button(microbiologia, text="Borrar",cursor="hand2",bg="#fd6418",relief="flat",width=12,font="ubuntu 10 ",fg="black", command=borrar)
    b4.place(x=558,y=418)
    b4.config(activebackground="#a65208", activeforeground="gray")

    microbiologia.config(menu=menubar)


    microbiologia.mainloop()

def home2():
    fisicoquimica = Toplevel(root)
    fisicoquimica.title("AREA FISICOQUIMICA")
    fisicoquimica.iconbitmap("graficos/logo.ico")
    fisicoquimica.geometry("1010x530+0+0")
    fisicoquimica.resizable(width=False, height=False)
    fisicoquimica.transient(root)
    
    tapiz = PhotoImage(file="graficos/interfaz.png")
    Label(fisicoquimica, image=tapiz).place(x=0, y=0, relwidth=1, relheight=1)

    
    vId=StringVar()
    vNombre=StringVar()
    vTipo=StringVar()
    vUmedida=StringVar()
    vCantidad=IntVar()
    vDescripcion=StringVar()
    vStockmin=IntVar()
    vStockmax=IntVar()
    vUbicacion=StringVar()
    vEtiquetacolor=StringVar()
    vEmpaque=StringVar()
    vCaracteristica=StringVar()
    vFechavencimiento=StringVar()
    vCategoriaseguridad=StringVar()
    vGarantia=StringVar()

    def conexionBBDD():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()

	    try:
		    miCursor.execute('''
			    CREATE TABLE fisicoquimica (
			    ID INTEGER PRIMARY KEY AUTOINCREMENT,
			    NOMBRE VARCHAR(50) NOT NULL,
			    TIPO VARCHAR(50) NOT NULL,
			    UNIDAD_DE_MEDIDA VARCHAR(50) NOT NULL,
			    CANTIDAD INTEGER NOT NULL,
			    DESCRIPCION VARCHAR(120) NOT NULL,
			    STOCKMIN INTEGER NOT NULL,
			    STOCKMAX INTEGER NOT NULL,
			    UBICACION VARCHAR(50) NOT NULL,
			    ETIQUETACOLOR VARCHAR(50),
			    EMPAQUE VARCHAR(50),
			    CARACTERISTICA VARCHAR(50),
			    FECHAVENCIMIENTO DATE,
			    CATEGORIASEGURIDAD VARCHAR(50),
			    GARANTIA VARCHAR(50))
			    ''')

		    messagebox.showinfo("CONEXION","Base de Datos Creada exitosamente")
	    except:
		    messagebox.showinfo("CONEXION", "Conexión exitosa con la base de datos")

    def eliminarBBDD():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    if messagebox.askyesno(message="¿Los Datos se perderan definitivamente, Desea continuar?", title="ADVERTENCIA"):
	       miCursor.execute("DROP TABLE fisicoquimica")
	    else:
		    pass
	    limpiarCampos()
	    mostrar()

    def salirAplicacion():
	    valor=messagebox.askquestion("Salir","¿Está seguro que desea salir de la Aplicación?")
	    if valor=="yes":
		    root.destroy()

    def limpiarCampos():
	    vId.set("")
	    vNombre.set("")
	    vTipo.set("")
	    vUmedida.set("")
	    vCantidad.set("")
	    vDescripcion.set("")
	    vStockmin.set("")
	    vStockmax.set("")
	    vUbicacion.set("")
	    vEtiquetacolor.set("")
	    vEmpaque.set("")
	    vCaracteristica.set("")
	    vFechavencimiento.set("")
	    vCategoriaseguridad.set("")
	    vGarantia.set("")

    def mensaje():
	    acerca='''
	    Gestor De Inventario
	    Area Ambiental SENA
	    Version 1.0
	    Tecnología Python Tkinter
	    '''
	    messagebox.showinfo(title="INFORMACION", message=acerca)

    ################################ Métodos CRUD ##############################

    def erroragregar():
        nom=vNombre.get()
        can=vCantidad.get()

        if(nom=='' and can==''):
            try:
                messagebox.showwarning("¡ups!","!No se pudo guardar! Algunos Campos son necesarios")
            except:
                pass
		
        
    def crear():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()

	    erroragregar()

	    nom=vNombre.get()
	    can=vCantidad.get()
    
            
	    if(nom!='' and can!=''):
	            try:
		            datos=vNombre.get(),vTipo.get(),vUmedida.get(),vCantidad.get(),vDescripcion.get(),vStockmin.get(),vStockmax.get(),vUbicacion.get(),vEtiquetacolor.get(),vEmpaque.get(),vCaracteristica.get(),vFechavencimiento.get(),vCategoriaseguridad.get(),vGarantia.get()
		            miCursor.execute("INSERT INTO fisicoquimica VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datos))
		            miConexion.commit()
	            except:
		            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con BBDD")
		            pass
	            limpiarCampos()
	            miConexion.close()
	            llamar()

    def mostrar1():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    registros=tree.get_children()
	    for elemento in registros:
		    tree.delete(elemento)

	    try:
		    miCursor.execute("SELECT * FROM fisicoquimica WHERE TIPO='Herramienta'")
		    for row in miCursor:
			    tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
	    except:
		    pass
    def mostrar2():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM fisicoquimica WHERE TIPO='Aseo'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass

    def mostrar3():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM fisicoquimica WHERE TIPO='Epp'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass



    def mostrar4():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM fisicoquimica WHERE TIPO='Producción'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass



    def mostrar5():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM fisicoquimica WHERE TIPO='S-Controladas'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass


    def mostrar6():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM fisicoquimica WHERE TIPO='S-Grupo E'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass


    def mostrar7():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM fisicoquimica WHERE TIPO='Otro'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass

    def mostrar():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM fisicoquimica")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass
    ################################## Tabla ################################
    seleccion=IntVar()		
    sel=seleccion.get()
    def llamar():
        if sel==1:
            mostrar1()
        elif sel==2:
            mostrar2()
        elif sel==3:
            mostrar3()
        elif sel==4:
            mostrar4()
        elif sel==5:
            mostrar5()
        elif sel==6:
            mostrar6()
        elif sel==7:
            mostrar7()
        elif sel==8:
            mostrar()

            
    		
    rb_frame= Frame(fisicoquimica,width=150, height=160)
    rb_frame.place(x=820, y=25)
    rb_frame.config(bg="#c0bebe")

    

    
    Radiobutton(rb_frame, 
                value=1,variable=seleccion,text="HERRAMIENTAS",cursor='hand2',bg="#c0bebe",command=mostrar1).place(x=0,y=0)
    Radiobutton(rb_frame,
                value=2,variable=seleccion,text="ASEO",cursor='hand2',bg="#c0bebe",command=mostrar2).place(x=0,y=20)
    Radiobutton(rb_frame, 
                value=3,variable=seleccion,text="EPP",cursor='hand2',bg="#c0bebe",command=mostrar3).place(x=0,y=40)
    Radiobutton(rb_frame, 
                value=4,variable=seleccion,text="PRODUCCIÓN",cursor='hand2',bg="#c0bebe",command=mostrar4).place(x=0,y=60)
    Radiobutton(rb_frame,
                value=5,variable=seleccion,text="S-CONTROLADAS",cursor='hand2',bg="#c0bebe", command=mostrar5).place(x=0,y=80)
    Radiobutton(rb_frame, 
                value=6,variable=seleccion,text="S-GRUPO E",cursor='hand2',bg="#c0bebe", command=mostrar6).place(x=0,y=100)
    Radiobutton(rb_frame, 
                value=7,variable=seleccion,text="OTROS",cursor='hand2',bg="#c0bebe", command=mostrar7).place(x=0,y=120)
    Radiobutton(rb_frame, 
                value=8,variable=seleccion,text="TODOS",cursor='hand2',bg="#c0bebe", command=mostrar).place(x=0,y=140)

		
    tree_frame = Frame(fisicoquimica)
    tree_frame.place(x=10,y=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    
    tree_scroll2 = Scrollbar(tree_frame,orient="horizontal")
    tree_scroll2.pack(side=BOTTOM,fill=X)

	
    tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,xscrollcommand=tree_scroll2.set,height=8, columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12','#13'))
    tree.pack()

    tree_scroll.config(command=tree.yview)
    tree_scroll2.config(command=tree.xview)



    tree.heading('#0', text="ID", anchor=CENTER)
    tree.column('#0',width=40,minwidth=60)
    tree.heading('#1', text="Nombre", anchor=CENTER)
    tree.column('#1', width=50,minwidth=100)
    tree.heading('#2', text="Tipo", anchor=CENTER)
    tree.column('#2', width=50,minwidth=100)
    tree.heading('#3', text="Unidad de Medida", anchor=CENTER)
    tree.column('#3', width=50,minwidth=110)
    tree.heading('#4', text="Cantidad", anchor=CENTER)
    tree.column('#4', width=50,minwidth=100)
    tree.heading('#5', text="Descripcion", anchor=CENTER)
    tree.column('#5', width=50,minwidth=100)
    tree.heading('#6', text="Stock minimo", anchor=CENTER)
    tree.column('#6', width=50,minwidth=100)
    tree.heading('#7', text="Stock maximo", anchor=CENTER)
    tree.column('#7', width=50,minwidth=100)
    tree.heading('#8', text="Ubicación", anchor=CENTER)
    tree.column('#8',width=50,minwidth=100)
    tree.heading('#9', text="Etiqueta de Color", anchor=CENTER)
    tree.column('#9', width=50,minwidth=100)
    tree.heading('#10', text="Empaque", anchor=CENTER)
    tree.column('#10', width=50,minwidth=100)
    tree.heading('#11', text="Estado Caracteristico", anchor=CENTER)
    tree.column('#11', width=50,minwidth=120)
    tree.heading('#12', text="Fecha de Vencimiento", anchor=CENTER)
    tree.column('#12', width=50,minwidth=130)
    tree.heading('#13', text="Categoria de Seguridad", anchor=CENTER)
    tree.column('#13', width=50,minwidth=135)
    tree.heading('#14', text="Garantia", anchor=CENTER)
    tree.column('#14', width=50,minwidth=100)


    def seleccionarUsandoClick(event):
	    item=tree.identify('item',event.x,event.y)
	    vId.set(tree.item(item,"text"))
	    vNombre.set(tree.item(item,"values")[0])
	    vTipo.set(tree.item(item,"values")[1])
	    vUmedida.set(tree.item(item,"values")[2])
	    vCantidad.set(tree.item(item,"values")[3])
	    vDescripcion.set(tree.item(item,"values")[4])
	    vStockmin.set(tree.item(item,"values")[5])
	    vStockmax.set(tree.item(item,"values")[6])
	    vUbicacion.set(tree.item(item,"values")[7])
	    vEtiquetacolor.set(tree.item(item,"values")[8])
	    vEmpaque.set(tree.item(item,"values")[9])
	    vCaracteristica.set(tree.item(item,"values")[10])
	    vFechavencimiento.set(tree.item(item,"values")[11])
	    vCategoriaseguridad.set(tree.item(item,"values")[12])
	    vGarantia.set(tree.item(item,"values")[13])

	
    tree.bind("<Double-1>", seleccionarUsandoClick)



    def actualizar():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    try:
		    datos=vNombre.get(),vTipo.get(),vUmedida.get(),vCantidad.get(),vDescripcion.get(),vStockmin.get(),vStockmax.get(),vUbicacion.get(),vEtiquetacolor.get(),vEmpaque.get(),vCaracteristica.get(),vFechavencimiento.get(),vCategoriaseguridad.get(),vGarantia.get()
		    miCursor.execute("UPDATE fisicoquimica SET NOMBRE=?, TIPO=?, UNIDAD_DE_MEDIDA=?, CANTIDAD=?, DESCRIPCION=?, STOCKMIN=?, STOCKMAX=?, UBICACION=?, ETIQUETACOLOR=?, EMPAQUE=?, CARACTERISTICA=?, FECHAVENCIMIENTO=?, CATEGORIASEGURIDAD=?, GARANTIA=? WHERE ID="+vId.get(), (datos))
		    miConexion.commit()
	    except:
		    messagebox.showwarning("ATENCIÓN","Seleccione un producto haciendo ¡Doble click!")
		    pass
	    limpiarCampos()
	    llamar()

    def borrar():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    try:
		    if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
			    miCursor.execute("DELETE FROM fisicoquimica WHERE ID="+vId.get())
			    miConexion.commit()
	    except:
		    messagebox.showwarning("ATENCIÓN","Seleccione un producto haciendo ¡Doble click!")
		    pass
	    limpiarCampos()
	    llamar()

    ###################### Colocar widgets en la VISTA ######################
    ########## Creando Los menus ###############
    menubar=Menu(fisicoquimica)
    menubasedat=Menu(menubar,tearoff=0)
    menubasedat.add_command(label="Crear/Conectar Base de Datos", command=conexionBBDD)
    menubasedat.add_command(label="Eliminar Base de Datos", command=eliminarBBDD)
    menubasedat.add_command(label="Salir", command=salirAplicacion)
    menubar.add_cascade(label="Inicio", menu=menubasedat)

    ayudamenu=Menu(menubar,tearoff=0)
    ayudamenu.add_command(label="Vaciar Campos", command=limpiarCampos)
    ayudamenu.add_command(label="Info", command=mensaje)
    menubar.add_cascade(label="Ayuda",menu=ayudamenu)

    loginmenu=Menu(menubar,tearoff=0)
    loginmenu.add_command(label="Registrar usuario", command=registrar)
    loginmenu.add_command(label="Ver usuarios", command=mensaje)
    loginmenu.add_command(label="Borrar usuarios", command=mensaje)
    menubar.add_cascade(label="Login",menu=loginmenu)

    ############## Creando etiquetas y cajas de texto ###########################
    
    c_estilos=ttk.Style()
    c_estilos.theme_use("clam")

    c_estilos.configure("TCombobox",
          background="#d6dce5",
          foreground="black",
          rowheight=25,
          fieldbackground="#d6dce5"            
          )
    c_estilos.map('TCombobox',
           background=[('selected','#d6dce5')])


    estilos = ttk.Style()

    estilos.theme_use("alt")

    estilos.configure("Treeview",
          background="#c0bebe",
          foreground="black",
          rowheight=21,
          fieldbackground="d6dce5"            
          )
    estilos.map('Treeview',
           background=[('selected','#fd6418')])
   

    
    e1=Entry(fisicoquimica, textvariable=vId)


    e2=Entry(fisicoquimica, textvariable=vNombre,bg="#d6dce5",relief="flat", width=16)
    e2.place(x=41,y=260)

    c1=ttk.Combobox(fisicoquimica,width=16,textvariable=vTipo,state="readonly",values=["Herramienta","Aseo","Epp","Producción","S-Controladas","S-Grupo E","Otro"])
    c1.place(x=205,y=260)
    
    c2=ttk.Combobox(fisicoquimica,width=16,textvariable=vUmedida,state="readonly",values=["Unidad","Kilogramos","C-cubicos","Centimetros","Litros"])
    c2.place(x=362,y=260)


    def valida_caracteres(action, char, text):
        if action != "1":
            return True
        return char in "0123456789." and len(text)< 7
    validatecommand = fisicoquimica.register(valida_caracteres)
    e5=Entry(fisicoquimica, validate="key",validatecommand=(validatecommand, "%d","%S","%s"), textvariable=vCantidad,bg="#d6dce5",relief="flat", width=7)
    e5.place(x=41,y=311)


    e6=Entry(fisicoquimica, textvariable=vDescripcion,bg="#d6dce5",relief="flat", width=16)
    e6.place(x=213,y=311)


    e7=Entry(fisicoquimica, validate="key",validatecommand=(validatecommand, "%d","%S","%s"),textvariable=vStockmin,bg="#d6dce5",relief="flat", width=11)
    e7.place(x=370,y=311)


    e8=Entry(fisicoquimica, validate="key",validatecommand=(validatecommand,"%d","%S","%s"),textvariable=vStockmax,bg="#d6dce5",relief="flat", width=12)
    e8.place(x=41,y=366)


    e9=Entry(fisicoquimica, textvariable=vUbicacion,bg="#d6dce5",relief="flat", width=16)
    e9.place(x=213,y=366)

    
    c3=ttk.Combobox(fisicoquimica,width=17,textvariable=vEtiquetacolor,state="readonly",values=["Rojo |","Rojo ||","Amarillo","Azul","Verde","No Aplica"])
    c3.place(x=360,y=366)
    CreateToolTip(c3, text = 'Rojo | -Muy Toxico\n'
                             'Rojo || -Toxico\n'
                             'Amarillo -Nocivo\n'
                             'Azul -Poco Peligroso\n'
                             'Verde -No ofrece peligro')

    e11=Entry(fisicoquimica, textvariable=vEmpaque,bg="#d6dce5",relief="flat", width=16)
    e11.place(x=41,y=420)


    e12=Entry(fisicoquimica, textvariable=vCaracteristica,bg="#d6dce5",relief="flat", width=16)
    e12.place(x=213,y=419)

    def valida_fecha(action, char, text):
        if action != "1":
            return True
        return char in "0123456789/" and len(text)< 10
    validatecommand = fisicoquimica.register(valida_fecha)
    e13=Entry(fisicoquimica,validate="key",validatecommand=(validatecommand, "%d","%S","%s"), textvariable=vFechavencimiento,bg="#d6dce5",relief="flat", width=19)
    e13.place(x=370,y=420)


    c4=ttk.Combobox(fisicoquimica,width=22,textvariable=vCategoriaseguridad,state="readonly",values=["Explosivas(EX)","Inflamables(IN)","Comburentes(CB)","Gas bajo presión(GZ)","Corrosivas(CR)","Toxic Aguda Cat-1(TO)","Toxic Aguda Cat-2(TO)","Toxic Aguda Cat-3(TO)","Toxic Aguda Cat-4(DA)","Mutageno(MU)","Dañ/med Ambiente(EN)","Ninguna"])
    c4.place(x=34,y=473)
    

    e15=Entry(fisicoquimica, textvariable=vGarantia,bg="#d6dce5",relief="flat", width=16)
    e15.place(x=213,y=473)



    ################# Creando botones ###########################

    b2=Button(fisicoquimica, text="Registrar",cursor="hand2",bg="#fd6418",relief="flat",width=12,font="ubuntu 10",fg="white", command=crear)
    b2.place(x=558,y=305)
    b2.config(activebackground="#a65208", activeforeground="gray")
    b3=Button(fisicoquimica, text="Modificar",cursor="hand2",bg="#fd6418",relief="flat",width=12,font="ubuntu 10",fg="white", command=actualizar)
    b3.place(x=558,y=363)
    b3.config(activebackground="#a65208", activeforeground="gray")
    b4=Button(fisicoquimica, text="Borrar",cursor="hand2",bg="#fd6418",relief="flat",width=12,font="ubuntu 10 ",fg="black", command=borrar)
    b4.place(x=558,y=418)
    b4.config(activebackground="#a65208", activeforeground="gray")

    fisicoquimica.config(menu=menubar)


    fisicoquimica.mainloop()


def home3():
    bioinsumo = Toplevel(root)
    bioinsumo.title("AREA BIOINSUMO")
    bioinsumo.iconbitmap("graficos/logo.ico")
    bioinsumo.geometry("1010x530+0+0")
    bioinsumo.resizable(width=False, height=False)
    bioinsumo.transient(root)
    
    tapiz = PhotoImage(file="graficos/interfaz.png")
    Label(bioinsumo, image=tapiz).place(x=0, y=0, relwidth=1, relheight=1)

    
    vId=StringVar()
    vNombre=StringVar()
    vTipo=StringVar()
    vUmedida=StringVar()
    vCantidad=IntVar()
    vDescripcion=StringVar()
    vStockmin=IntVar()
    vStockmax=IntVar()
    vUbicacion=StringVar()
    vEtiquetacolor=StringVar()
    vEmpaque=StringVar()
    vCaracteristica=StringVar()
    vFechavencimiento=StringVar()
    vCategoriaseguridad=StringVar()
    vGarantia=StringVar()

    def conexionBBDD():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()

	    try:
		    miCursor.execute('''
			    CREATE TABLE bioinsumo (
			    ID INTEGER PRIMARY KEY AUTOINCREMENT,
			    NOMBRE VARCHAR(50) NOT NULL,
			    TIPO VARCHAR(50) NOT NULL,
			    UNIDAD_DE_MEDIDA VARCHAR(50) NOT NULL,
			    CANTIDAD INTEGER NOT NULL,
			    DESCRIPCION VARCHAR(120) NOT NULL,
			    STOCKMIN INTEGER NOT NULL,
			    STOCKMAX INTEGER NOT NULL,
			    UBICACION VARCHAR(50) NOT NULL,
			    ETIQUETACOLOR VARCHAR(50),
			    EMPAQUE VARCHAR(50),
			    CARACTERISTICA VARCHAR(50),
			    FECHAVENCIMIENTO DATE,
			    CATEGORIASEGURIDAD VARCHAR(50),
			    GARANTIA VARCHAR(50))
			    ''')

		    messagebox.showinfo("CONEXION","Base de Datos Creada exitosamente")
	    except:
		    messagebox.showinfo("CONEXION", "Conexión exitosa con la base de datos")

    def eliminarBBDD():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    if messagebox.askyesno(message="¿Los Datos se perderan definitivamente, Desea continuar?", title="ADVERTENCIA"):
	       miCursor.execute("DROP TABLE bioinsumo")
	    else:
		    pass
	    limpiarCampos()
	    mostrar()

    def salirAplicacion():
	    valor=messagebox.askquestion("Salir","¿Está seguro que desea salir de la Aplicación?")
	    if valor=="yes":
		    root.destroy()

    def limpiarCampos():
	    vId.set("")
	    vNombre.set("")
	    vTipo.set("")
	    vUmedida.set("")
	    vCantidad.set("")
	    vDescripcion.set("")
	    vStockmin.set("")
	    vStockmax.set("")
	    vUbicacion.set("")
	    vEtiquetacolor.set("")
	    vEmpaque.set("")
	    vCaracteristica.set("")
	    vFechavencimiento.set("")
	    vCategoriaseguridad.set("")
	    vGarantia.set("")

    def mensaje():
	    acerca='''
	    Gestor De Inventario
	    Area Ambiental SENA
	    Version 1.0
	    Tecnología Python Tkinter
	    '''
	    messagebox.showinfo(title="INFORMACION", message=acerca)

    ################################ Métodos CRUD ##############################

    def erroragregar():
        nom=vNombre.get()
        can=vCantidad.get()

        if(nom=='' and can==''):
            try:
                messagebox.showwarning("¡ups!","!No se pudo guardar! Algunos Campos son necesarios")
            except:
                pass
		
        
    def crear():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()

	    erroragregar()

	    nom=vNombre.get()
	    can=vCantidad.get()
    
            
	    if(nom!='' and can!=''):
	            try:
		            datos=vNombre.get(),vTipo.get(),vUmedida.get(),vCantidad.get(),vDescripcion.get(),vStockmin.get(),vStockmax.get(),vUbicacion.get(),vEtiquetacolor.get(),vEmpaque.get(),vCaracteristica.get(),vFechavencimiento.get(),vCategoriaseguridad.get(),vGarantia.get()
		            miCursor.execute("INSERT INTO bioinsumo VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datos))
		            miConexion.commit()
	            except:
		            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con BBDD")
		            pass
	            limpiarCampos()
	            miConexion.close()
	            llamar()

    def mostrar1():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    registros=tree.get_children()
	    for elemento in registros:
		    tree.delete(elemento)

	    try:
		    miCursor.execute("SELECT * FROM bioinsumo WHERE TIPO='Herramienta'")
		    for row in miCursor:
			    tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
	    except:
		    pass
    def mostrar2():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM bioinsumo WHERE TIPO='Aseo'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass

    def mostrar3():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM bioinsumo WHERE TIPO='Epp'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass



    def mostrar4():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM bioinsumo WHERE TIPO='Producción'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass



    def mostrar5():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM bioinsumo WHERE TIPO='S-Controladas'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass


    def mostrar6():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM bioinsumo WHERE TIPO='S-Grupo E'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass


    def mostrar7():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM bioinsumo WHERE TIPO='Otro'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass

    def mostrar():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM bioinsumo")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass
    ################################## Tabla ################################
    seleccion=IntVar()		
    sel=seleccion.get()
    def llamar():
        if sel==1:
            mostrar1()
        elif sel==2:
            mostrar2()
        elif sel==3:
            mostrar3()
        elif sel==4:
            mostrar4()
        elif sel==5:
            mostrar5()
        elif sel==6:
            mostrar6()
        elif sel==7:
            mostrar7()
        elif sel==8:
            mostrar()

            
    		
    rb_frame= Frame(bioinsumo,width=150, height=160)
    rb_frame.place(x=820, y=25)
    rb_frame.config(bg="#c0bebe")

    

    
    Radiobutton(rb_frame, 
                value=1,variable=seleccion,text="HERRAMIENTAS",cursor='hand2',bg="#c0bebe",command=mostrar1).place(x=0,y=0)
    Radiobutton(rb_frame,
                value=2,variable=seleccion,text="ASEO",cursor='hand2',bg="#c0bebe",command=mostrar2).place(x=0,y=20)
    Radiobutton(rb_frame, 
                value=3,variable=seleccion,text="EPP",cursor='hand2',bg="#c0bebe",command=mostrar3).place(x=0,y=40)
    Radiobutton(rb_frame, 
                value=4,variable=seleccion,text="PRODUCCIÓN",cursor='hand2',bg="#c0bebe",command=mostrar4).place(x=0,y=60)
    Radiobutton(rb_frame,
                value=5,variable=seleccion,text="S-CONTROLADAS",cursor='hand2',bg="#c0bebe", command=mostrar5).place(x=0,y=80)
    Radiobutton(rb_frame, 
                value=6,variable=seleccion,text="S-GRUPO E",cursor='hand2',bg="#c0bebe", command=mostrar6).place(x=0,y=100)
    Radiobutton(rb_frame, 
                value=7,variable=seleccion,text="OTROS",cursor='hand2',bg="#c0bebe", command=mostrar7).place(x=0,y=120)
    Radiobutton(rb_frame, 
                value=8,variable=seleccion,text="TODOS",cursor='hand2',bg="#c0bebe", command=mostrar).place(x=0,y=140)

		
    tree_frame = Frame(bioinsumo)
    tree_frame.place(x=10,y=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    
    tree_scroll2 = Scrollbar(tree_frame,orient="horizontal")
    tree_scroll2.pack(side=BOTTOM,fill=X)

	
    tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,xscrollcommand=tree_scroll2.set,height=8, columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12','#13'))
    tree.pack()

    tree_scroll.config(command=tree.yview)
    tree_scroll2.config(command=tree.xview)



    tree.heading('#0', text="ID", anchor=CENTER)
    tree.column('#0',width=40,minwidth=60)
    tree.heading('#1', text="Nombre", anchor=CENTER)
    tree.column('#1', width=50,minwidth=100)
    tree.heading('#2', text="Tipo", anchor=CENTER)
    tree.column('#2', width=50,minwidth=100)
    tree.heading('#3', text="Unidad de Medida", anchor=CENTER)
    tree.column('#3', width=50,minwidth=110)
    tree.heading('#4', text="Cantidad", anchor=CENTER)
    tree.column('#4', width=50,minwidth=100)
    tree.heading('#5', text="Descripcion", anchor=CENTER)
    tree.column('#5', width=50,minwidth=100)
    tree.heading('#6', text="Stock minimo", anchor=CENTER)
    tree.column('#6', width=50,minwidth=100)
    tree.heading('#7', text="Stock maximo", anchor=CENTER)
    tree.column('#7', width=50,minwidth=100)
    tree.heading('#8', text="Ubicación", anchor=CENTER)
    tree.column('#8',width=50,minwidth=100)
    tree.heading('#9', text="Etiqueta de Color", anchor=CENTER)
    tree.column('#9', width=50,minwidth=100)
    tree.heading('#10', text="Empaque", anchor=CENTER)
    tree.column('#10', width=50,minwidth=100)
    tree.heading('#11', text="Estado Caracteristico", anchor=CENTER)
    tree.column('#11', width=50,minwidth=120)
    tree.heading('#12', text="Fecha de Vencimiento", anchor=CENTER)
    tree.column('#12', width=50,minwidth=130)
    tree.heading('#13', text="Categoria de Seguridad", anchor=CENTER)
    tree.column('#13', width=50,minwidth=135)
    tree.heading('#14', text="Garantia", anchor=CENTER)
    tree.column('#14', width=50,minwidth=100)


    def seleccionarUsandoClick(event):
	    item=tree.identify('item',event.x,event.y)
	    vId.set(tree.item(item,"text"))
	    vNombre.set(tree.item(item,"values")[0])
	    vTipo.set(tree.item(item,"values")[1])
	    vUmedida.set(tree.item(item,"values")[2])
	    vCantidad.set(tree.item(item,"values")[3])
	    vDescripcion.set(tree.item(item,"values")[4])
	    vStockmin.set(tree.item(item,"values")[5])
	    vStockmax.set(tree.item(item,"values")[6])
	    vUbicacion.set(tree.item(item,"values")[7])
	    vEtiquetacolor.set(tree.item(item,"values")[8])
	    vEmpaque.set(tree.item(item,"values")[9])
	    vCaracteristica.set(tree.item(item,"values")[10])
	    vFechavencimiento.set(tree.item(item,"values")[11])
	    vCategoriaseguridad.set(tree.item(item,"values")[12])
	    vGarantia.set(tree.item(item,"values")[13])

	
    tree.bind("<Double-1>", seleccionarUsandoClick)



    def actualizar():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    try:
		    datos=vNombre.get(),vTipo.get(),vUmedida.get(),vCantidad.get(),vDescripcion.get(),vStockmin.get(),vStockmax.get(),vUbicacion.get(),vEtiquetacolor.get(),vEmpaque.get(),vCaracteristica.get(),vFechavencimiento.get(),vCategoriaseguridad.get(),vGarantia.get()
		    miCursor.execute("UPDATE bioinsumo SET NOMBRE=?, TIPO=?, UNIDAD_DE_MEDIDA=?, CANTIDAD=?, DESCRIPCION=?, STOCKMIN=?, STOCKMAX=?, UBICACION=?, ETIQUETACOLOR=?, EMPAQUE=?, CARACTERISTICA=?, FECHAVENCIMIENTO=?, CATEGORIASEGURIDAD=?, GARANTIA=? WHERE ID="+vId.get(), (datos))
		    miConexion.commit()
	    except:
		    messagebox.showwarning("ATENCIÓN","Seleccione un producto haciendo ¡Doble click!")
		    pass
	    limpiarCampos()
	    llamar()

    def borrar():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    try:
		    if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
			    miCursor.execute("DELETE FROM bioinsumo WHERE ID="+vId.get())
			    miConexion.commit()
	    except:
		    messagebox.showwarning("ATENCIÓN","Seleccione un producto haciendo ¡Doble click!")
		    pass
	    limpiarCampos()
	    llamar()

    ###################### Colocar widgets en la VISTA ######################
    ########## Creando Los menus ###############
    menubar=Menu(bioinsumo)
    menubasedat=Menu(menubar,tearoff=0)
    menubasedat.add_command(label="Crear/Conectar Base de Datos", command=conexionBBDD)
    menubasedat.add_command(label="Eliminar Base de Datos", command=eliminarBBDD)
    menubasedat.add_command(label="Salir", command=salirAplicacion)
    menubar.add_cascade(label="Inicio", menu=menubasedat)

    ayudamenu=Menu(menubar,tearoff=0)
    ayudamenu.add_command(label="Vaciar Campos", command=limpiarCampos)
    ayudamenu.add_command(label="Info", command=mensaje)
    menubar.add_cascade(label="Ayuda",menu=ayudamenu)

    loginmenu=Menu(menubar,tearoff=0)
    loginmenu.add_command(label="Registrar usuario", command=registrar)
    loginmenu.add_command(label="Ver usuarios", command=mensaje)
    loginmenu.add_command(label="Borrar usuarios", command=mensaje)
    menubar.add_cascade(label="Login",menu=loginmenu)

    ############## Creando etiquetas y cajas de texto ###########################
    
    c_estilos=ttk.Style()
    c_estilos.theme_use("clam")

    c_estilos.configure("TCombobox",
          background="#d6dce5",
          foreground="black",
          rowheight=25,
          fieldbackground="#d6dce5"            
          )
    c_estilos.map('TCombobox',
           background=[('selected','#d6dce5')])


    estilos = ttk.Style()

    estilos.theme_use("alt")

    estilos.configure("Treeview",
          background="#c0bebe",
          foreground="black",
          rowheight=21,
          fieldbackground="d6dce5"            
          )
    estilos.map('Treeview',
           background=[('selected','#fd6418')])
   

    
    e1=Entry(bioinsumo, textvariable=vId)


    e2=Entry(bioinsumo, textvariable=vNombre,bg="#d6dce5",relief="flat", width=16)
    e2.place(x=41,y=260)

    c1=ttk.Combobox(bioinsumo,width=16,textvariable=vTipo,state="readonly",values=["Herramienta","Aseo","Epp","Producción","S-Controladas","S-Grupo E","Otro"])
    c1.place(x=205,y=260)
    
    c2=ttk.Combobox(bioinsumo,width=16,textvariable=vUmedida,state="readonly",values=["Unidad","Kilogramos","C-cubicos","Centimetros","Litros"])
    c2.place(x=362,y=260)


    def valida_caracteres(action, char, text):
        if action != "1":
            return True
        return char in "0123456789." and len(text)< 7
    validatecommand = bioinsumo.register(valida_caracteres)
    e5=Entry(bioinsumo, validate="key",validatecommand=(validatecommand, "%d","%S","%s"), textvariable=vCantidad,bg="#d6dce5",relief="flat", width=7)
    e5.place(x=41,y=311)


    e6=Entry(bioinsumo, textvariable=vDescripcion,bg="#d6dce5",relief="flat", width=16)
    e6.place(x=213,y=311)


    e7=Entry(bioinsumo, validate="key",validatecommand=(validatecommand, "%d","%S","%s"),textvariable=vStockmin,bg="#d6dce5",relief="flat", width=11)
    e7.place(x=370,y=311)


    e8=Entry(bioinsumo, validate="key",validatecommand=(validatecommand,"%d","%S","%s"),textvariable=vStockmax,bg="#d6dce5",relief="flat", width=12)
    e8.place(x=41,y=366)


    e9=Entry(bioinsumo, textvariable=vUbicacion,bg="#d6dce5",relief="flat", width=16)
    e9.place(x=213,y=366)

    
    c3=ttk.Combobox(bioinsumo,width=17,textvariable=vEtiquetacolor,state="readonly",values=["Rojo |","Rojo ||","Amarillo","Azul","Verde","No Aplica"])
    c3.place(x=360,y=366)
    CreateToolTip(c3, text = 'Rojo | -Muy Toxico\n'
                             'Rojo || -Toxico\n'
                             'Amarillo -Nocivo\n'
                             'Azul -Poco Peligroso\n'
                             'Verde -No ofrece peligro')

    e11=Entry(bioinsumo, textvariable=vEmpaque,bg="#d6dce5",relief="flat", width=16)
    e11.place(x=41,y=420)


    e12=Entry(bioinsumo, textvariable=vCaracteristica,bg="#d6dce5",relief="flat", width=16)
    e12.place(x=213,y=419)

    def valida_fecha(action, char, text):
        if action != "1":
            return True
        return char in "0123456789/" and len(text)< 10
    validatecommand = bioinsumo.register(valida_fecha)
    e13=Entry(bioinsumo,validate="key",validatecommand=(validatecommand, "%d","%S","%s"), textvariable=vFechavencimiento,bg="#d6dce5",relief="flat", width=19)
    e13.place(x=370,y=420)


    c4=ttk.Combobox(bioinsumo,width=22,textvariable=vCategoriaseguridad,state="readonly",values=["Explosivas(EX)","Inflamables(IN)","Comburentes(CB)","Gas bajo presión(GZ)","Corrosivas(CR)","Toxic Aguda Cat-1(TO)","Toxic Aguda Cat-2(TO)","Toxic Aguda Cat-3(TO)","Toxic Aguda Cat-4(DA)","Mutageno(MU)","Dañ/med Ambiente(EN)","Ninguna"])
    c4.place(x=34,y=473)
    

    e15=Entry(bioinsumo, textvariable=vGarantia,bg="#d6dce5",relief="flat", width=16)
    e15.place(x=213,y=473)



    ################# Creando botones ###########################
    
    b2=Button(bioinsumo, text="Registrar",cursor="hand2",bg="#fd6418",relief="flat",width=12,font="ubuntu 10",fg="white", command=crear)
    b2.place(x=558,y=305)
    b2.config(activebackground="#a65208", activeforeground="gray")
    b3=Button(bioinsumo, text="Modificar",cursor="hand2",bg="#fd6418",relief="flat",width=12,font="ubuntu 10",fg="white", command=actualizar)
    b3.place(x=558,y=363)
    b3.config(activebackground="#a65208", activeforeground="gray")
    b4=Button(bioinsumo, text="Borrar",cursor="hand2",bg="#fd6418",relief="flat",width=12,font="ubuntu 10 ",fg="black", command=borrar)
    b4.place(x=558,y=418)
    b4.config(activebackground="#a65208", activeforeground="gray")

    bioinsumo.config(menu=menubar)


    bioinsumo.mainloop()


def home4():
    florayfauna = Toplevel(root)
    florayfauna.title("AREA FLORA Y FAUNA")
    florayfauna.iconbitmap("graficos/logo.ico")
    florayfauna.geometry("1010x530+0+0")
    florayfauna.resizable(width=False, height=False)
    florayfauna.transient(root)
    
    tapiz = PhotoImage(file="graficos/interfaz.png")
    Label(florayfauna, image=tapiz).place(x=0, y=0, relwidth=1, relheight=1)

    
    vId=StringVar()
    vNombre=StringVar()
    vTipo=StringVar()
    vUmedida=StringVar()
    vCantidad=IntVar()
    vDescripcion=StringVar()
    vStockmin=IntVar()
    vStockmax=IntVar()
    vUbicacion=StringVar()
    vEtiquetacolor=StringVar()
    vEmpaque=StringVar()
    vCaracteristica=StringVar()
    vFechavencimiento=StringVar()
    vCategoriaseguridad=StringVar()
    vGarantia=StringVar()

    def conexionBBDD():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()

	    try:
		    miCursor.execute('''
			    CREATE TABLE florayfauna (
			    ID INTEGER PRIMARY KEY AUTOINCREMENT,
			    NOMBRE VARCHAR(50) NOT NULL,
			    TIPO VARCHAR(50) NOT NULL,
			    UNIDAD_DE_MEDIDA VARCHAR(50) NOT NULL,
			    CANTIDAD INTEGER NOT NULL,
			    DESCRIPCION VARCHAR(120) NOT NULL,
			    STOCKMIN INTEGER NOT NULL,
			    STOCKMAX INTEGER NOT NULL,
			    UBICACION VARCHAR(50) NOT NULL,
			    ETIQUETACOLOR VARCHAR(50),
			    EMPAQUE VARCHAR(50),
			    CARACTERISTICA VARCHAR(50),
			    FECHAVENCIMIENTO DATE,
			    CATEGORIASEGURIDAD VARCHAR(50),
			    GARANTIA VARCHAR(50))
			    ''')

		    messagebox.showinfo("CONEXION","Base de Datos Creada exitosamente")
	    except:
		    messagebox.showinfo("CONEXION", "Conexión exitosa con la base de datos")

    def eliminarBBDD():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    if messagebox.askyesno(message="¿Los Datos se perderan definitivamente, Desea continuar?", title="ADVERTENCIA"):
	       miCursor.execute("DROP TABLE florayfauna")
	    else:
		    pass
	    limpiarCampos()
	    mostrar()

    def salirAplicacion():
	    valor=messagebox.askquestion("Salir","¿Está seguro que desea salir de la Aplicación?")
	    if valor=="yes":
		    root.destroy()

    def limpiarCampos():
	    vId.set("")
	    vNombre.set("")
	    vTipo.set("")
	    vUmedida.set("")
	    vCantidad.set("")
	    vDescripcion.set("")
	    vStockmin.set("")
	    vStockmax.set("")
	    vUbicacion.set("")
	    vEtiquetacolor.set("")
	    vEmpaque.set("")
	    vCaracteristica.set("")
	    vFechavencimiento.set("")
	    vCategoriaseguridad.set("")
	    vGarantia.set("")

    def mensaje():
	    acerca='''
	    Gestor De Inventario
	    Area Ambiental SENA
	    Version 1.0
	    Tecnología Python Tkinter
	    '''
	    messagebox.showinfo(title="INFORMACION", message=acerca)

    ################################ Métodos CRUD ##############################

    def erroragregar():
        nom=vNombre.get()
        can=vCantidad.get()

        if(nom=='' and can==''):
            try:
                messagebox.showwarning("¡ups!","!No se pudo guardar! Algunos Campos son necesarios")
            except:
                pass
		
        
    def crear():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()

	    erroragregar()

	    nom=vNombre.get()
	    can=vCantidad.get()
    
            
	    if(nom!='' and can!=''):
	            try:
		            datos=vNombre.get(),vTipo.get(),vUmedida.get(),vCantidad.get(),vDescripcion.get(),vStockmin.get(),vStockmax.get(),vUbicacion.get(),vEtiquetacolor.get(),vEmpaque.get(),vCaracteristica.get(),vFechavencimiento.get(),vCategoriaseguridad.get(),vGarantia.get()
		            miCursor.execute("INSERT INTO florayfauna VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datos))
		            miConexion.commit()
	            except:
		            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con BBDD")
		            pass
	            limpiarCampos()
	            miConexion.close()
	            llamar()

    def mostrar1():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    registros=tree.get_children()
	    for elemento in registros:
		    tree.delete(elemento)

	    try:
		    miCursor.execute("SELECT * FROM florayfauna WHERE TIPO='Herramienta'")
		    for row in miCursor:
			    tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
	    except:
		    pass
    def mostrar2():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM florayfauna WHERE TIPO='Aseo'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass

    def mostrar3():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM florayfauna WHERE TIPO='Epp'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass



    def mostrar4():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM florayfauna WHERE TIPO='Producción'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass



    def mostrar5():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM florayfauna WHERE TIPO='S-Controladas'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass


    def mostrar6():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM florayfauna WHERE TIPO='S-Grupo E'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass


    def mostrar7():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM florayfauna WHERE TIPO='Otro'")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass

    def mostrar():
        miConexion=sqlite3.connect("base.db")
        miCursor=miConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM florayfauna")
            for row in miCursor:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        except:
            pass
    ################################## Tabla ################################
    seleccion=IntVar()		
    sel=seleccion.get()
    def llamar():
        if sel==1:
            mostrar1()
        elif sel==2:
            mostrar2()
        elif sel==3:
            mostrar3()
        elif sel==4:
            mostrar4()
        elif sel==5:
            mostrar5()
        elif sel==6:
            mostrar6()
        elif sel==7:
            mostrar7()
        elif sel==8:
            mostrar()

            
    		
    rb_frame= Frame(florayfauna,width=150, height=160)
    rb_frame.place(x=820, y=25)
    rb_frame.config(bg="#c0bebe")

    

    
    Radiobutton(rb_frame, 
                value=1,variable=seleccion,text="HERRAMIENTAS",cursor='hand2',bg="#c0bebe",command=mostrar1).place(x=0,y=0)
    Radiobutton(rb_frame,
                value=2,variable=seleccion,text="ASEO",cursor='hand2',bg="#c0bebe",command=mostrar2).place(x=0,y=20)
    Radiobutton(rb_frame, 
                value=3,variable=seleccion,text="EPP",cursor='hand2',bg="#c0bebe",command=mostrar3).place(x=0,y=40)
    Radiobutton(rb_frame, 
                value=4,variable=seleccion,text="PRODUCCIÓN",cursor='hand2',bg="#c0bebe",command=mostrar4).place(x=0,y=60)
    Radiobutton(rb_frame,
                value=5,variable=seleccion,text="S-CONTROLADAS",cursor='hand2',bg="#c0bebe", command=mostrar5).place(x=0,y=80)
    Radiobutton(rb_frame, 
                value=6,variable=seleccion,text="S-GRUPO E",cursor='hand2',bg="#c0bebe", command=mostrar6).place(x=0,y=100)
    Radiobutton(rb_frame, 
                value=7,variable=seleccion,text="OTROS",cursor='hand2',bg="#c0bebe", command=mostrar7).place(x=0,y=120)
    Radiobutton(rb_frame, 
                value=8,variable=seleccion,text="TODOS",cursor='hand2',bg="#c0bebe", command=mostrar).place(x=0,y=140)

		
    tree_frame = Frame(florayfauna)
    tree_frame.place(x=10,y=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    
    tree_scroll2 = Scrollbar(tree_frame,orient="horizontal")
    tree_scroll2.pack(side=BOTTOM,fill=X)

	
    tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,xscrollcommand=tree_scroll2.set,height=8, columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12','#13'))
    tree.pack()

    tree_scroll.config(command=tree.yview)
    tree_scroll2.config(command=tree.xview)



    tree.heading('#0', text="ID", anchor=CENTER)
    tree.column('#0',width=40,minwidth=60)
    tree.heading('#1', text="Nombre", anchor=CENTER)
    tree.column('#1', width=50,minwidth=100)
    tree.heading('#2', text="Tipo", anchor=CENTER)
    tree.column('#2', width=50,minwidth=100)
    tree.heading('#3', text="Unidad de Medida", anchor=CENTER)
    tree.column('#3', width=50,minwidth=110)
    tree.heading('#4', text="Cantidad", anchor=CENTER)
    tree.column('#4', width=50,minwidth=100)
    tree.heading('#5', text="Descripcion", anchor=CENTER)
    tree.column('#5', width=50,minwidth=100)
    tree.heading('#6', text="Stock minimo", anchor=CENTER)
    tree.column('#6', width=50,minwidth=100)
    tree.heading('#7', text="Stock maximo", anchor=CENTER)
    tree.column('#7', width=50,minwidth=100)
    tree.heading('#8', text="Ubicación", anchor=CENTER)
    tree.column('#8',width=50,minwidth=100)
    tree.heading('#9', text="Etiqueta de Color", anchor=CENTER)
    tree.column('#9', width=50,minwidth=100)
    tree.heading('#10', text="Empaque", anchor=CENTER)
    tree.column('#10', width=50,minwidth=100)
    tree.heading('#11', text="Estado Caracteristico", anchor=CENTER)
    tree.column('#11', width=50,minwidth=120)
    tree.heading('#12', text="Fecha de Vencimiento", anchor=CENTER)
    tree.column('#12', width=50,minwidth=130)
    tree.heading('#13', text="Categoria de Seguridad", anchor=CENTER)
    tree.column('#13', width=50,minwidth=135)
    tree.heading('#14', text="Garantia", anchor=CENTER)
    tree.column('#14', width=50,minwidth=100)


    def seleccionarUsandoClick(event):
	    item=tree.identify('item',event.x,event.y)
	    vId.set(tree.item(item,"text"))
	    vNombre.set(tree.item(item,"values")[0])
	    vTipo.set(tree.item(item,"values")[1])
	    vUmedida.set(tree.item(item,"values")[2])
	    vCantidad.set(tree.item(item,"values")[3])
	    vDescripcion.set(tree.item(item,"values")[4])
	    vStockmin.set(tree.item(item,"values")[5])
	    vStockmax.set(tree.item(item,"values")[6])
	    vUbicacion.set(tree.item(item,"values")[7])
	    vEtiquetacolor.set(tree.item(item,"values")[8])
	    vEmpaque.set(tree.item(item,"values")[9])
	    vCaracteristica.set(tree.item(item,"values")[10])
	    vFechavencimiento.set(tree.item(item,"values")[11])
	    vCategoriaseguridad.set(tree.item(item,"values")[12])
	    vGarantia.set(tree.item(item,"values")[13])

	
    tree.bind("<Double-1>", seleccionarUsandoClick)



    def actualizar():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    try:
		    datos=vNombre.get(),vTipo.get(),vUmedida.get(),vCantidad.get(),vDescripcion.get(),vStockmin.get(),vStockmax.get(),vUbicacion.get(),vEtiquetacolor.get(),vEmpaque.get(),vCaracteristica.get(),vFechavencimiento.get(),vCategoriaseguridad.get(),vGarantia.get()
		    miCursor.execute("UPDATE florayfauna SET NOMBRE=?, TIPO=?, UNIDAD_DE_MEDIDA=?, CANTIDAD=?, DESCRIPCION=?, STOCKMIN=?, STOCKMAX=?, UBICACION=?, ETIQUETACOLOR=?, EMPAQUE=?, CARACTERISTICA=?, FECHAVENCIMIENTO=?, CATEGORIASEGURIDAD=?, GARANTIA=? WHERE ID="+vId.get(), (datos))
		    miConexion.commit()
	    except:
		    messagebox.showwarning("ATENCIÓN","Seleccione un producto haciendo ¡Doble click!")
		    pass
	    limpiarCampos()
	    llamar()

    def borrar():
	    miConexion=sqlite3.connect("base.db")
	    miCursor=miConexion.cursor()
	    try:
		    if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
			    miCursor.execute("DELETE FROM florayfauna WHERE ID="+vId.get())
			    miConexion.commit()
	    except:
		    messagebox.showwarning("ATENCIÓN","Seleccione un producto haciendo ¡Doble click!")
		    pass
	    limpiarCampos()
	    llamar()

    ###################### Colocar widgets en la VISTA ######################
    ########## Creando Los menus ###############
    menubar=Menu(florayfauna)
    menubasedat=Menu(menubar,tearoff=0)
    menubasedat.add_command(label="Crear/Conectar Base de Datos", command=conexionBBDD)
    menubasedat.add_command(label="Eliminar Base de Datos", command=eliminarBBDD)
    menubasedat.add_command(label="Salir", command=salirAplicacion)
    menubar.add_cascade(label="Inicio", menu=menubasedat)

    ayudamenu=Menu(menubar,tearoff=0)
    ayudamenu.add_command(label="Vaciar Campos", command=limpiarCampos)
    ayudamenu.add_command(label="Info", command=mensaje)
    menubar.add_cascade(label="Ayuda",menu=ayudamenu)

    loginmenu=Menu(menubar,tearoff=0)
    loginmenu.add_command(label="Registrar usuario", command=registrar)
    loginmenu.add_command(label="Ver usuarios", command=mensaje)
    loginmenu.add_command(label="Borrar usuarios", command=mensaje)
    menubar.add_cascade(label="Login",menu=loginmenu)

    ############## Creando etiquetas y cajas de texto ###########################
    
    c_estilos=ttk.Style()
    c_estilos.theme_use("clam")

    c_estilos.configure("TCombobox",
          background="#d6dce5",
          foreground="black",
          rowheight=25,
          fieldbackground="#d6dce5"            
          )
    c_estilos.map('TCombobox',
           background=[('selected','#d6dce5')])


    estilos = ttk.Style()

    estilos.theme_use("alt")

    estilos.configure("Treeview",
          background="#c0bebe",
          foreground="black",
          rowheight=21,
          fieldbackground="d6dce5"            
          )
    estilos.map('Treeview',
           background=[('selected','#fd6418')])
   

    
    e1=Entry(florayfauna, textvariable=vId)


    e2=Entry(florayfauna, textvariable=vNombre,bg="#d6dce5",relief="flat", width=16)
    e2.place(x=41,y=260)

    c1=ttk.Combobox(florayfauna,width=16,textvariable=vTipo,state="readonly",values=["Herramienta","Aseo","Epp","Producción","S-Controladas","S-Grupo E","Otro"])
    c1.place(x=205,y=260)
    
    c2=ttk.Combobox(florayfauna,width=16,textvariable=vUmedida,state="readonly",values=["Unidad","Kilogramos","C-cubicos","Centimetros","Litros"])
    c2.place(x=362,y=260)


    def valida_caracteres(action, char, text):
        if action != "1":
            return True
        return char in "0123456789." and len(text)< 7
    validatecommand = florayfauna.register(valida_caracteres)
    e5=Entry(florayfauna, validate="key",validatecommand=(validatecommand, "%d","%S","%s"), textvariable=vCantidad,bg="#d6dce5",relief="flat", width=7)
    e5.place(x=41,y=311)


    e6=Entry(florayfauna, textvariable=vDescripcion,bg="#d6dce5",relief="flat", width=16)
    e6.place(x=213,y=311)


    e7=Entry(florayfauna, validate="key",validatecommand=(validatecommand, "%d","%S","%s"),textvariable=vStockmin,bg="#d6dce5",relief="flat", width=11)
    e7.place(x=370,y=311)


    e8=Entry(florayfauna, validate="key",validatecommand=(validatecommand,"%d","%S","%s"),textvariable=vStockmax,bg="#d6dce5",relief="flat", width=12)
    e8.place(x=41,y=366)


    e9=Entry(florayfauna, textvariable=vUbicacion,bg="#d6dce5",relief="flat", width=16)
    e9.place(x=213,y=366)

    
    c3=ttk.Combobox(florayfauna,width=17,textvariable=vEtiquetacolor,state="readonly",values=["Rojo |","Rojo ||","Amarillo","Azul","Verde","No Aplica"])
    c3.place(x=360,y=366)
    CreateToolTip(c3, text = 'Rojo | -Muy Toxico\n'
                             'Rojo || -Toxico\n'
                             'Amarillo -Nocivo\n'
                             'Azul -Poco Peligroso\n'
                             'Verde -No ofrece peligro')

    e11=Entry(florayfauna, textvariable=vEmpaque,bg="#d6dce5",relief="flat", width=16)
    e11.place(x=41,y=420)


    e12=Entry(florayfauna, textvariable=vCaracteristica,bg="#d6dce5",relief="flat", width=16)
    e12.place(x=213,y=419)

    def valida_fecha(action, char, text):
        if action != "1":
            return True
        return char in "0123456789/" and len(text)< 10
    validatecommand = florayfauna.register(valida_fecha)
    e13=Entry(florayfauna,validate="key",validatecommand=(validatecommand, "%d","%S","%s"), textvariable=vFechavencimiento,bg="#d6dce5",relief="flat", width=19)
    e13.place(x=370,y=420)


    c4=ttk.Combobox(florayfauna,width=22,textvariable=vCategoriaseguridad,state="readonly",values=["Explosivas(EX)","Inflamables(IN)","Comburentes(CB)","Gas bajo presión(GZ)","Corrosivas(CR)","Toxic Aguda Cat-1(TO)","Toxic Aguda Cat-2(TO)","Toxic Aguda Cat-3(TO)","Toxic Aguda Cat-4(DA)","Mutageno(MU)","Dañ/med Ambiente(EN)","Ninguna"])
    c4.place(x=34,y=473)
    

    e15=Entry(florayfauna, textvariable=vGarantia,bg="#d6dce5",relief="flat", width=16)
    e15.place(x=213,y=473)



    ################# Creando botones ###########################
    
    b2=Button(florayfauna, text="Registrar",cursor="hand2",bg="#fd6418",relief="flat",width=12,font="ubuntu 10",fg="white", command=crear)
    b2.place(x=558,y=305)
    b2.config(activebackground="#a65208", activeforeground="gray")
    b3=Button(florayfauna, text="Modificar",cursor="hand2",bg="#fd6418",relief="flat",width=12,font="ubuntu 10",fg="white", command=actualizar)
    b3.place(x=558,y=363)
    b3.config(activebackground="#a65208", activeforeground="gray")
    b4=Button(florayfauna, text="Borrar",cursor="hand2",bg="#fd6418",relief="flat",width=12,font="ubuntu 10 ",fg="black", command=borrar)
    b4.place(x=558,y=418)
    b4.config(activebackground="#a65208", activeforeground="gray")

    florayfauna.config(menu=menubar)


    florayfauna.mainloop()

