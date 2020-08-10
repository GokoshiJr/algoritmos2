# 2. Contar la cantidad de dígitos que tiene un número. 

num = int(input('Ingrese un numero: '))
contador = 0
aux = num

while (aux > 0):    
    aux //= 10
    contador += 1
    
print('Su numero tiene ', contador, 'digitos.')
