import cv2
from tkinter import *

ventana=Tk()
ventana.title('Daniela Galicia Osuna')
ventana.geometry('500x400')
    
def pic():
    camara = cv2.VideoCapture(0)

    leido, frame = camara.read()

    if leido == True:
        cv2.imwrite('Daniela Osuna.png',frame)
        print('se tomo con exito la foto')

        foto=PhotoImage(file='Daniela Osuna.png')
        soy=Label(ventana, image=foto).place(x=0,y=0)
        
    else:
        print('Error Camara no existe o esta apagada o no esta configurada')

    def ca():
        ventana.destroy()

    boton1=Button(ventana, text='Nueva Foto', command=pic)
    boton1.place (x=10, y=10)

    boton2=Button(ventana, text='Bye', command=ventana.destroy)
    boton2.place (x=10, y=100)
    ventana.mainloop() 
        
pic()
