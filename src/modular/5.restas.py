# 5. Encuentre el cociente y el residuo de dos números mayores a cero dados en base a restas sucesivas. Ejemplo: Si A = 435 y B = 21 → Cociente = 20 y Residuo = 15 

num1 = int(input('Ingrese A: '))
num2 = int(input('Ingrese B: '))

def division(numerador, denominador):
    temp = numerador
    cociente = residuo = 0
    while(temp >= 0):
        temp = temp - denominador 
        if(temp >= 0):
            residuo = temp
            cociente += 1
    print('Cociente:', cociente, 'Residuo: ', residuo)

if((num1 > 0) & (num2 > 0)):
    division(num1, num2)    
else:
    print('No se puede realizar la operacion ambos numeros deben ser mayores a 0.')
