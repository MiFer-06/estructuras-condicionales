'''Comparación de tres números
    Solicita tres números y muestra cuál es el mayor y cuál es el menor.
'''

num1 = float(input('Ingresa un numero: ' ))
num2 = float(input('Ingresa un numero: '))
num3 = float(input('Ingresa un numero: '))
    
if num1 > num2 and num1 > num3:
    print(f"El número {num1} es el mayor")
elif num2 > num1 and num2 > num3:
    print(f"El número {num2} es el mayor")
elif num3 > num1 and num3 > num2:
    print(f"El número {num3} es el mayor")
elif num1 == num2 and num1 > num3:
    print(f"Los números {num1} y {num2} son los mayores e iguales")
elif num1 == num3 and num1 > num2:
    print(f"Los números {num1} y {num3} son los mayores e iguales")
elif num2 == num3 and num2 > num1:
    print(f"Los números {num2} y {num3} son los mayores e iguales")
elif num1 == num2 and num2 == num3:
    print(f"Los tres números son iguales: {num1}")
    
else:
    print('No se puede hacer una comparación')