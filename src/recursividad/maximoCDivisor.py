# 6. Escribir un programa que calcule el máximo común divisor (MCD) de dos enteros positivos. 
# Si  M >=  N una función recursiva para MCD es:  MCD = M si N = 0
#
# MCD = MCD (N, M mod N) si N <> 0  El programa le debe permitir al usuario ingresar 
# los valores para M y N desde la consola. Una función recursiva es entonces llamada 
# para calcular el MCD. El programa entonces imprime el valor para el MCD. 
#
# Si el usuario ingresa un valor para M que es < que N el programa es responsable de 
# switchear los valores. 

def maximoDivisor(m, n):
    if (m < n):
        temp = m
        m = n
        n = temp
        return maximoDivisor(n, (m % n))
    elif (m >= n):
        if (n == 0):
            return (m)
        else:    
            return maximoDivisor(n, (m % n))

m = int(input('Ingrese el num1:'))
n = int(input('Ingrese el num2:'))
print(maximoDivisor(m, n))
