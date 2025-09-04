#Clasificación de triángulos- Solicita al usuario las 3 longitudes de los lados de un triángulo.
#Indica si es equilátero, isósceles o escaleno.
 # Si los tres lados son iguales, es un triángulo equilátero
 # Si no, pero al menos dos lados son iguales, es isósceles
 # Si ninguno de los lados es igual, es escaleno

lado1= float(input('Ingresa la medida uno del triangulo:  '))
lado2= float(input('Ingresa la medida dos del triangulo:  '))
lado3= float(input('Ingresa la medida tres del triangulo  '))

# Verificar si las longitudes pueden formar un triángulo válido
# La suma de dos lados debe ser mayor que el tercero para cada combinación
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3>lado1):
    
    
    if lado1 == lado2 ==lado3:
        print('El triangulo es Equilátero, ya que todos sus lados son iguales.  ')
        
    elif lado1==lado2 or lado1 == lado3 or lado2==lado3:
        print('es un triangulo isóseles ya que dos de sus lados son iguales. ')
        
else:
    print('Es un triangulo escaleno, ya que ninguno de sus lados son iguales')

