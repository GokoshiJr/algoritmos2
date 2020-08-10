# 8. Calcule la suma de los divisores de un número. 
# Ejemplo: Si n = 4 → Se devuelve 7 (1+2+4 = 7) 

def divisores(num):
    divisor = i = sumatoria = 0
    for i in range (1, num + 1):
        if (num % i == 0):
            divisor = i
            sumatoria = sumatoria + divisor            
    return sumatoria

num = int(input('Ingrese un numero entero: '))
print('La sumatoria de sus divisores es', divisores(num))
