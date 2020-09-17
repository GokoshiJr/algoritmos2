# Algoritmos de Ordenacion - Seleccion

numeros = [9,5,6,3,1,2,4,7,8]
minimo = 0
def seleccion(numArray):
    for i in range (0, len(numArray) - 1):
        minimo = i
        for j in range (i + 1, len(numArray)):
            if numArray[j] < numArray[minimo]:
                minimo = j
        temporal = numArray[i]
        numArray[i] = numArray[minimo]
        numArray[minimo] = temporal
    return numArray

ordenado = seleccion(numeros)
print(ordenado)