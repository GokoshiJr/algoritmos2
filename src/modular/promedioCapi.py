# 14. Leer un lote de N números y determine el promedio de múltiplos de 7 que contengan, 
# cuántos son capicúas (Si el número y su inverso son iguales).
# Ejemplo: Si N = 8 [49, 2, 7, 34, 55, 105, 121, 53]
# → Promedio de Múltiplos de 7: 53.67 
# Cantidad de Capicúas: 4

def capicua(numero):
    aux = numero
    result = 0
    while (aux > 0):
        digito = aux % 10    
        result = (result * 10) + digito     
        aux //= 10
    if (numero == result):
        return (True)
    else: 
        return (False)

def divisores7(arrayNum):
    sumatoria = contador = 0
    for i in range(len(arrayNum)):
        if (numeros[i] % 7 == 0):   
            sumatoria += arrayNum[i]
            contador += 1 
    return (sumatoria/contador)

def mostrar(arrayNum):
    contador = 0
    for i in range(len(arrayNum)):           
        if (capicua(arrayNum[i])):
            contador += 1    
    print('Promedio de multiplos de 7: {:.2f}'.format(divisores7(arrayNum)))
    print('Cantidad de capicuas {:d}'.format(contador))

numeros = [49, 2, 7, 34, 55, 105, 121, 53]
mostrar(numeros)
