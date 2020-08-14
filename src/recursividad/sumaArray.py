# 9. Programe un método recursivo que calcule la suma de un arreglo de números enteros.

def sumaArray(numArray, n):
    if (n == 0):
        return (0)
    else:
        return (numArray[n - 1] + sumaArray(numArray, n - 1))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(sumaArray(numeros, len(numeros)))
