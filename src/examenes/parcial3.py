#!/usr/bin/env python3

""" 
Se leen dos listas de números enteros, A y B de n y m elementos, respectivamente (2 ptos). 
Se desea resolver mediante procedimientos las siguientes tareas:

a) Ordenar, aplicando el método de inserción, cada una de las listas A y B (4 ptos).
b) Crear una lista C, ya ordenada, por intercalación o mezcla de las listas A y B (12 ptos).
c) Visualizar la lista C ordenada (2 ptos).

Escribir un programa Python que realice esta tarea 
"""

def insercion(numArray: list) -> list:
    for i in range(1, len(numArray)):
        aux = i
        while (aux > 0 and numArray[aux - 1] > numArray[aux]):
            numArray[aux], numArray[aux - 1] = (
                numArray[aux - 1],
                numArray[aux],
            )
            aux -= 1
    return numArray

def mezclaDosArrays(izq: list, der: list) -> list:
    numArray = []    
    while (len(izq) > 0 and len(der) > 0):
        if (izq[0] < der[0]):
            numArray.append(izq.pop(0))
        else:
            numArray.append(der.pop(0))
    while (len(izq) > 0):
        numArray.append(izq.pop(0))
    while (len(der) > 0):
        numArray.append((der.pop(0)))
    return numArray

if __name__ == "__main__":

    # Parcial 3 Algoritmos y Estructuras 2 305C1    

    print('\n\tExamen Parcial 3 - Algoritmos de Ordenacion')
    arrayA = [6, 1, 4, 2, 7, 12, 20, 15, 10, 19, 5]
    arrayB = [9, 8, 12, 2, 10, 6, 15, 22, 1, 0, 3, 4]
    print("\n\tArrays Cargados:")
    print(f"\t{arrayA = }")
    print(f"\t{arrayB = }")

    # Punto A - Ordenar, aplicando el método de inserción, cada una de las listas A y B.
    print('\n\tPunto A')
    print(f"\t{insercion(arrayA) = }")
    print(f"\t{insercion(arrayB) = }")

    # Punto B - Crear una lista C, ya ordenada, por intercalación o mezcla de las listas A y B.   
    arrayC = mezclaDosArrays(arrayA, arrayB)

    # Punto C - Visualizar la lista C ordenada.
    print('\n\tPunto C')
    print(f"\t{arrayC = }")

    print('\n\tFin del Programa...\n')
