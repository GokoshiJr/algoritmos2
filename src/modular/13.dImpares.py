# 13. Leer un número que tenga exactamente 6 dígitos, y elimine todos los dígitos impares que tenga. Ejemplo: Si N = 123456 → N = 246

def impar(num):
    aux = num
    digito = 0
    array = []
    while (aux > 0):
        digito = aux % 10
        aux //= 10
        if (digito % 2 == 0):            
            array.append(digito)
    array.reverse()
    return (array)

def escribirNum(numeros):
    aux = 0
    for i in range (len(numeros)):    
        aux = (aux * 10) + numeros[i]    
    return (aux)

num = int(input('Indique un numero:'))
numeros = impar(num)
print(escribirNum(numeros))
