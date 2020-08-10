# 7. Determine si un número es primo o no. Devuelva 1 si es primo y 0 en caso contrario.

def primo(num):
    contador = 0        
    for i in range (1, num + 1):        
        if (num % i == 0):
            contador += 1
    if (contador == 2):
        return (1)
    else:
        return (0)

num = int(input('Indique un numero: '))
print(primo(num))
