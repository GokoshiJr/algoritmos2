# 3. Invertir un numero

numero = int(input('Ingrese un numero: '))
digito = result = 0
aux = numero

while(aux > 0):
    digito = aux % 10    
    result = (result * 10) + digito     
    aux //= 10

print('Su inverso es:', result)
