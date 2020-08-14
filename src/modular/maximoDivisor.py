# 6. Encuentre el máximo común divisor de dos números. Ejemplo: Si A = 145 y B = 100 el mcd = 5 

def maximoDivisor(a, b): 
    mayor = menor = resto = 0
    if (a < b):
        menor = a
        mayor = b
    else:
        mayor = a
        menor = b
    while (menor != 0):
        resto = mayor % menor
        mayor = menor
        menor = resto
    return (mayor)

a = int(input('Ingrese el valor de A: '))
b = int(input('Ingrese el valor de B: '))
print('El mcd es :', maximoDivisor(a, b))
    