from tkinter import *
ventana=Tk()
ventana.title('imagenes')
ventana.geometry('400x300')
foto=PhotoImage(file='covid-19.png')
fondo=Label(ventana, image=foto).place(x=0,y=0)
ventana.mainloop()






                
