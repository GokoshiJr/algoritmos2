# 4. Determinar si un número es múltiplo de k. Si es así devuelva 1 y 0 en caso contrario. 
# Ejemplo. Si n = 42 y k = 7 → se devuelve 1 (porque 42 es múltiplo de 7) 

num = div = 0
base = int(input('Ingrese la base: '))
multiplo = int(input('Ingrese el multiplo: '))

def multi(b, m):
    div = base // multiplo
    for i in range (div):
        num = m * (i + 1)        
    if (num == b):
        return (1)
    else:
        return (0)
print(multi(base, multiplo))
