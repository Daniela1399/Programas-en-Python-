class Estados:
    pass
coahuila = Estados()
guanajuato = Estados()
jalisco = Estados()
chiapas = Estados()

Estados=['coahuila','guanajuato','jalisco','chiapas']

p=input('¿Que estado quieres elegir? ')

coahuila.confirmados = 27331
coahuila.negativos = 36896
coahuila.defunciones = 1934
coahuila.recuperados = 21278

guanajuato.confirmados = 41955
guanajuato.negativos = 58676
guanajuato.defunciones = 2982
guanajuato.recuperados = 32543

jalisco.confirmados = 28128
jalisco.negativos = 38013
jalisco.defunciones = 3396
jalisco.recuperados = 17024

chiapas.confirmados = 6579
chiapas.negativos = 5310
chiapas.defunciones = 1090
chiapas.recuperados = 4023

if p == 'coahuila':
    print('Confirmados:', coahuila.confirmados)
    print('Negativos:', coahuila.negativos)
    print('Defunciones', coahuila.defunciones)
    print('Recuperados', coahuila.recuperados)

elif p == 'guanajuato':
    print('Confirmados:', guanajuato.confirmados)
    print('Negativos:', guanajuato.negativos)
    print('Defunciones', guanajuato.defunciones)
    print('Recuperados', guanajuato.recuperados)

elif p == 'jalisco':
    print('Confirmados:', jalisco.confirmados)
    print('Negativos:', jalisco.negativos)
    print('Defunciones', jalisco.defunciones)
    print('Recuperados', jalisco.recuperados)

elif p == 'chiapas':
    print('Confirmados:', chiapas.confirmados)
    print('Negativos:', chiapas.negativos)
    print('Defunciones', chiapas.defunciones)
    print('Recuperados', chiapas.recuperados)

else:
    print('Este estado no se encuentra')





    

    
