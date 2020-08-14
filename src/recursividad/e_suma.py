# 4. Escribir una función recursiva que devuelva la suma de los primeros N enteros

def suma(num):
    if(num == 1):
        return (1)
    else:
        return num + suma(num-1)

print(suma(9))