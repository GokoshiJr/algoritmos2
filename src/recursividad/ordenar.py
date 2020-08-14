# 3. Escriba una función recursiva que ordene de menor a mayor un arreglo de enteros 
# basándose en la siguiente idea: coloque el elemento más pequeño en 
# la primera ubicación, y luego ordene el resto
# del arreglo con una llamada recursiva.

# n = len(numArray)
def bubbleSort(numArray, n):
    if (n == 1):
        return (numArray)
    else:
        for i in range (1, n - 1):
            if (numArray[i] > numArray[i + 1]):
                temp = numArray[i]
                numArray[i] = numArray[i + 1]
                numArray[i + 1] = temp
        return (bubbleSort(numArray, n - 1))

def littleFirst(numArray):
    orden = [min(numArray)]
    array.remove(min(numArray))
    orden += numArray
    return (orden)

array = [64, 34, 25, 12, 22, 45, 11, 90]
orden = littleFirst(array)
print(bubbleSort(orden, len(orden)))
