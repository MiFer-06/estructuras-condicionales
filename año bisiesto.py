'''  Año bisiesto.  Solicita un año e indica si es bisiesto o no.
    (Un año es bisiesto si es divisible entre 4 pero no entre 100, o si es divisible entre 400).
'''

año = int(input('Ingrese un año: '))

if (año%4) ==0:
    print('Es un año bisiesto')
    
else:
    print('El año capturado NO es bisiesto.')
    