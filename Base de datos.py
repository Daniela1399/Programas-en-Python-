from tkinter import *
from tkinter.ttk import *
import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="covd"
)
mycursor= mydb.cursor()

ventana=Tk()
ventana.title("PAGINA PRINCIPAL")
ventana.geometry("550x400")
imagen= PhotoImage(file="coronavirus19.png")
fondo =Label(ventana,image=imagen).place(x=0,y=0)

def coahuila():

    mycursor.execute("SELECT * FROM estadisticas where ControlD='1'")
    myresult= mycursor.fetchall()

    a=myresult[0][0]
    b=myresult[0][1]
    c=myresult[0][2]
    d=myresult[0][3]

    print("")
    ventana.destroy()
    ventana.__init__()
    ventana.geometry("550x250")
    ventana.title("COAHUILA")
        
    eti=Label(ventana, text="ControlD      Confirmados       Fallecidos       Recuperados")
    eti.place(x=93,y=50)
    et=Label(ventana, text=a)
    et.place(x=115, y=70)
    et=Label(ventana, text=b)
    et.place(x=180, y=70)
    et=Label(ventana, text=c)
    et.place(x=260, y=70)
    et=Label(ventana, text=d)
    et.place(x=335, y=70)

    boton=Button(ventana,text="Salir",command=salir)
    boton.place(x=210,y=140)

def guanajuato():

    mycursor.execute("SELECT * FROM estadisticas where ControlD='2'")
    myresult= mycursor.fetchall()

    a=myresult[0][0]
    b=myresult[0][1]
    c=myresult[0][2]
    d=myresult[0][3]

    print("")
    ventana.destroy()
    ventana.__init__()
    ventana.geometry('550x250')
    ventana.title("GUANAJUATO")


    eti=Label(ventana, text="ControlD      Confirmados       Fallecidos       Recuperados")
    eti.place(x=93,y=50)
    et=Label(ventana, text=a)
    et.place(x=115, y=70)
    et=Label(ventana, text=b)
    et.place(x=180, y=70)
    et=Label(ventana, text=c)
    et.place(x=260, y=70)
    et=Label(ventana, text=d)
    et.place(x=335, y=70)
    
    boton=Button(ventana,text="Salir",command=salir)
    boton.place(x=210,y=140)

def jalisco():
    mycursor.execute("SELECT * FROM estadisticas where ControlD='3'")
    myresult= mycursor.fetchall()

    a=myresult[0][0]
    b=myresult[0][1]
    c=myresult[0][2]
    d=myresult[0][3]

    print("")
    ventana.destroy()
    ventana.__init__()
    ventana.geometry("550x250")
    ventana.title("JALISCO")
        
    eti=Label(ventana, text="ControlD      Confirmados       Fallecidos       Recuperados")
    eti.place(x=93,y=50)
    et=Label(ventana, text=a)
    et.place(x=115, y=70)
    et=Label(ventana, text=b)
    et.place(x=180, y=70)
    et=Label(ventana, text=c)
    et.place(x=260, y=70)
    et=Label(ventana, text=d)
    et.place(x=335, y=70)
    
    boton=Button(ventana,text="Salir",command=salir)
    boton.place(x=210,y=140)

def chiapas():
    mycursor.execute("SELECT * FROM estadisticas where ControlD='4'")
    myresult= mycursor.fetchall()

    a=myresult[0][0]
    b=myresult[0][1]
    c=myresult[0][2]
    d=myresult[0][3]

    print("")
    ventana.destroy()
    ventana.__init__()
    ventana.geometry("550x250")
    ventana.title("CHIAPAS")
        
    eti=Label(ventana, text="ControlD      Confirmados       Fallecidos       Recuperados")
    eti.place(x=93,y=50)
    et=Label(ventana, text=a)
    et.place(x=115, y=70)
    et=Label(ventana, text=b)
    et.place(x=180, y=70)
    et=Label(ventana, text=c)
    et.place(x=260, y=70)
    et=Label(ventana, text=d)
    et.place(x=335, y=70)
    
    boton=Button(ventana,text="Salir",command=salir)
    boton.place(x=210,y=140)


def oaxaca():
    mycursor.execute("SELECT * FROM estadisticas where ControlD='5'")
    myresult= mycursor.fetchall()

    a=myresult[0][0]
    b=myresult[0][1]
    c=myresult[0][2]
    d=myresult[0][3]

    print("")
    ventana.destroy()
    ventana.__init__()
    ventana.geometry("550x250")
    ventana.title("OAXACA")
        
    eti=Label(ventana, text="ControlD      Confirmados       Fallecidos       Recuperados")
    eti.place(x=93,y=50)
    et=Label(ventana, text=a)
    et.place(x=115, y=70)
    et=Label(ventana, text=b)
    et.place(x=180, y=70)
    et=Label(ventana, text=c)
    et.place(x=260, y=70)
    et=Label(ventana, text=d)
    et.place(x=335, y=70)
    
    boton=Button(ventana,text="Salir",command=salir)
    boton.place(x=210,y=140)
 
def salir():
    ventana.destroy()

def agg():
     ventana.destroy()
     ventana.__init__()
     def guardar():
          mycursor.execute("SELECT MAX (ControlD) AS maximum FROM ControlE")
          result = mycursor.fetchall()
          for i in result:
               x=i[0]
          x=x+1
          sql=("""INSERT INTO estados (ControlD,ControlE) VALUES (%s,%s)""")
          val= (x,estados.get())
          sqll = ("""INSERT INTO estadisticas (ControlD      Confirmados       Fallecidos     Recuperados) VALUES (%s,%s,%s,%s) """)
          vall = (x,Confirmados.get(),Fallecidos.get(),Recuperados.get())
          mycursor.execute(sql, val)
          mycursor.execute(sqll, vall)
          mydb.commit()
          ventana.destroy()
          ventana.__init__()
          ventana.title("Agregar")
          ventana.geometry("525x250")
          eti=Label(ventana, text="Se guardo correctamente")
          eti.place(x=220,y=20)
          boton=Button(ventana,text="Salir",command=salir)
          boton.place(x=250,y=180)
          
     ventana.title("Agregar")
     ventana.geometry("525x250")

     etiqueta=Label(ventana,text="Nombre:")
     etiqueta.place(x=30,y=20)
     etiqueta=Label(ventana,text="Confirmados:")
     etiqueta.place(x=25,y=50)
     etiqueta=Label(ventana,text="Fallecidos:")
     etiqueta.place(x=30,y=80)
     etiqueta=Label(ventana,text="Recuperados:")
     etiqueta.place(x=30,y=110)

     Nombre=StringVar()
     cajatexto=Entry(ventana,textvariable=Nombre)
     cajatexto.place(x=105,y=20)
     Confirmados=IntVar()
     cajatexto=Entry(ventana,textvariable=Confirmados)
     cajatexto.place(x=105,y=50)
     Fallecidos=IntVar()
     cajatexto=Entry(ventana,textvariable=Fallecidos)
     cajatexto.place(x=105,y=80)
     Recuperados=IntVar()
     cajatexto=Entry(ventana,textvariable=Recuperados)
     cajatexto.place(x=105,y=110)
     
     boton=Button(ventana,text="Guardar",command=guardar)
     boton.place(x=235,y=180)


    
b1=Button(ventana,text="COAHUILA",command=coahuila).place(x=227,y=50)
b2=Button(ventana,text="GUANAJUATO",command=guanajuato).place(x=220,y=100)
b3=Button(ventana,text="JALISCO",command=jalisco).place(x=227,y=150)
b4=Button(ventana,text="CHIAPAS",command=chiapas).place(x=227,y=200)
b5=Button(ventana,text="OAXACA",command=oaxaca).place(x=227,y=250)
b6=Button(ventana,text="AGREGAR UN ESTADO",command=agg).place(x=200,y=300)

ventana.mainloop()

