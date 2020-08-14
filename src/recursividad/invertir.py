# 10. Programe un método recursivo que invierta los números de un arreglo de enteros. 

def invertir(numArray):
    if (len(numArray) == 0):
        return []
    else:
        return ([numArray[-1]] + invertir(numArray[:-1]))       

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(invertir(numeros))
