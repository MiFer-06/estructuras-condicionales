'''Conversor de calificaciones
Pide una calificación numérica (0–100) y muestra la equivalencia en letra:
  90–100: A
  80–89: B
  70–79: C
  60–69: D
   Menor a 60: F'''
   
calificacion = int(input('Ingresa tu calificación:  '))

if calificacion >= 90:
    print('Su calificasion es de: ',calificacion,'A  (Destacado).') 
    
elif calificacion >= 80:
    print('Su calificasion es de:',calificacion,'B (Satisfactoria).')

elif calificacion >= 70:
    print('Su calificasion es de:',calificacion,'C (suficiente).')

else:
    calificacion >= 60
    print('Su calificasion es de:',calificacion,'D (Insuficiente).')

