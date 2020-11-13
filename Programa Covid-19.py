from tkinter import *
from tkinter.ttk import*
import json

def lineaSearch(item,my_list):
    found = False
    position = 0
    while position < len(my_list) and not found:
        if my_list[position] == item:
            found = True
        position = position + 1
    return found


bolsa=['Coahuila','Guanajuato','Jalisco','Chiapas','Durango','Oaxaca','Aguascalientes','Nuevo Leon','Quintana Roo','Zacatecas']

window = Tk()
window.title('ESTADOS')
window.geometry("450x295")

foto=PhotoImage(file='covid-19.png')
fondo=Label(window, image=foto).place(x=0, y=0)

selected = IntVar()

est1= Radiobutton(window, text='Coahuila', value=1, variable=selected)
est1.pack( anchor = W)
est2= Radiobutton(window, text='Guanajuato', value=2, variable=selected)
est2.pack( anchor = W)
est3= Radiobutton(window, text='Jalisco', value=3, variable=selected)
est3.pack( anchor = W)
est4= Radiobutton(window, text='Chiapas', value=4, variable=selected)
est4.pack( anchor = W)
est5= Radiobutton(window, text='Durango', value=5, variable=selected)
est5.pack( anchor = W)
est6= Radiobutton(window, text='Oaxaca', value=6, variable=selected)
est6.pack( anchor = W)
est7= Radiobutton(window, text='Aguascalientes', value=7, variable=selected)
est7.pack( anchor = W)
est8= Radiobutton(window, text='Nuevo Leon', value=8, variable=selected)
est8.pack( anchor = W)
est9= Radiobutton(window, text='Quintana Roo', value=9, variable=selected)
est9.pack( anchor = W)
est10= Radiobutton(window, text='Zacatecas', value=10, variable=selected)
est10.pack( anchor = W)

def clicked():
    
    if(selected.get())==1:
        item=('--Coahuila--')
        data ={}
        data['--Coahuila--']=[]
            
        data['--Coahuila--'].append({
            'Confirmados': 27331,
            'Negativos': 36896,
            'Defunciones': 1934,
            'Recuperados': 21278})

    elif(selected.get())==2:
        item=('--Guanajuato--')
        data={}
        data['--Guanajuato--']=[]

        data['--Guanajuato--'].append({
            'Confirmados': 41955,
            'Negativos': 58676,
            'Defunciones': 2982,
            'Recuperados': 32543})
        
    elif(selected.get())==3:
        item=('--Jalisco--')
        data={}
        data['--Jalisco--']=[]

        data['--Jalisco--'].append({
            'Confirmados': 28128,
            'Negativos': 38013,
            'Defunciones': 3396,
            'Recuperados': 17024})
    
    elif(selected.get())==4:
        item=('--Chiapas--')
        data={}
        data['--Chiapas--']=[]

        data['--Chiapas--'].append({
            'Confirmados': 6579,
            'Negativos': 5310,
            'Defunciones': 1090,
            'Recuperados': 4023})

    elif(selected.get())==5:
        item=('--Durango--')
        data={}
        data['--Durango--']=[]

        data['--Durango--'].append({
            'Confirmados': 9467,
            'Negativos': 15991,
            'Defunciones': 654,
            'Recuperados': 6887})
   
    elif(selected.get())==6:
        item=('--Oaxaca--')
        data={}
        data['--Oaxaca--']=[]

        data['--Oaxaca--'].append({
            'Confirmados': 17513,
            'Negativos': 7594,
            'Defunciones': 1479,
            'Recuperados': 12734})
        
    elif(selected.get())==7:
        item=('--Aguascalientes--')
        data={}
        data['--Aguascalientes--']=[]
            
        data['--Aguascalientes--'].append({
            'Confirmados': 7545,
            'Negativos': 14792,
            'Defunciones': 647,
            'Recuperados': 4969})

    elif(selected.get())==8:
        item=('--Nuevo Leon--')
        data={}
        data['--Nuevo Leon--']=[]

        data['--Nuevo Leon--'].append({
            'Confirmados': 41843,
            'Negativos': 48175,
            'Defunciones': 3161,
            'Recuperados': 29167})

    elif(selected.get())==9:
        item=('--Quintana Roo--')
        data={}
        data['--Quintana Roo--']=[]

        data['--Quintana Roo--'].append({
            'Confirmados': 12156,
            'Negativos': 8245,
            'Defunciones': 1688,
            'Recuperados': 8095})

    elif(selected.get())==10:
        item=('--Zacatecas--')
        data={}
        data['--Zacatecas--']=[]

        data['--Zacatecas--'].append({
            'Confirmados': 7777,
            'Negativos': 8977,
            'Defunciones': 752,
            'Recuperados': 5289})

    for c in data[item]:
        print(item)
        print('Confirmados', c['Confirmados'])
        print('Negativos', c['Negativos'])
        print ('Defunciones', c['Defunciones'])
        print ('Recuperados', c['Recuperados'])
        print('')

        with open('Estados Covid-19 de '+item,'w') as file:
                json.dump(data[item],file)
        with open('Estados Covid-19 de '+item) as file:
                data=json.load(file)
                

btn= Button(window, text='Buscar', command=clicked)
btn.place(x=160, y=220)

window.mainloop()
