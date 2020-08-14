# 5. Escribir un programa que encuentre la suma de los enteros positivos pares desde 2 hasta N.
# Chequear que si N es impar se imprima un mensaje de error. 

def sumaPar(num):
    if (num == 0):
        return (0) 
    elif (num % 2 == 1):
        print('Error')
        return (sumaPar(num-1))
    elif (num % 2 == 0):        
        return (num + sumaPar(num-2))

print(sumaPar(9))
