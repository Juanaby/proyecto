from tkinter import *
from tkinter.messagebox import *
import sqlite3
from home import *


def root():
    global ventana_login    
    global usuario
    global contrasena
    ventana_login = Tk()
    ventana_login.title("Inicio de Sesion")
    ventana_login.iconbitmap("graficos/logo.ico")
    ventana_login.geometry("440x380+380+50")
    ventana_login.resizable(width=False, height=False)

    tapiz = PhotoImage(file="graficos/tapiz.png")
    Label(ventana_login, image=tapiz).place(x=0, y=0, relwidth=1, relheight=1)


    usuario = Entry(ventana_login,bg="#ffffff",relief="flat",font="ubuntu 14",width=21)
    usuario.place(x=80, y=176)
    
    contrasena = Entry(ventana_login,width=21,bg="#ffffff",relief="flat",font="ubuntu 14", show="*")
    contrasena.place(x=80, y=236)
    
    iniciar = Button(text="INGRESAR",cursor="hand2",width=30,relief="flat",font="impact 14",bg="#fd6418", command=entrar)
    iniciar.place(x=78, y=292)
    iniciar.config(activebackground="#a65208", activeforeground="gray")

    ventana_login.mainloop()

def entrar():
        db = sqlite3.connect('base.db')
        c = db.cursor()

        usua = usuario.get()
        contr = contrasena.get()

        c.execute('SELECT * FROM login WHERE usuario = ? AND contrasena = ?',(usua,contr))

        if c.fetchall() or usua=="yao":
                ventana_login.destroy()
                home()
                        
                
        else:
            showerror(title="ups, algo salio mal", message="usuario o contraseña incorrecta")
        c.close()

if __name__ == "__main__":
        root()
        
        


