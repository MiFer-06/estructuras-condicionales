'''Tarifa de entrada
Solicita la edad de una persona y muestra el costo de entrada a un parque:
Menores de 12 años: $50
De 12 a 17 años: $80
Adultos (18 en adelante): $120
'''

edad=int(input('Ingresa tu edad: '))

if edad<13:
    print('Por ser menor de edad tu entrada costara: $50')
elif edad<=17:
    print('Los adolecentes pagan: $80')
else:
    edad>17
    print('Los adultos pagan: $120')
    
    