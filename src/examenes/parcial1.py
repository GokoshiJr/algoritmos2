# Examen Parcial 1 Algoritmos y Estructuras 2 Seccion 305C1 

# ----- Programacion Modular -----

def factorial(numero):
    fact = 1
    for i in range (1, numero + 1):
        fact *= i
    return (fact)

def coseno(num, termino):
    bandera = True
    result = 1 

    if(termino % 2 == 0):    
        for i in range (2, termino + 2, 2): 
            if(bandera):
                result -= pow(num, i) / factorial(i) 
                bandera = False
            else:
                result += pow(num, i) / factorial(i)
                bandera = True

    if((termino % 2 == 1) & (termino > 1)):    
        for i in range (2, termino + 2, 2):  
            if(bandera):
                result -= pow(num, i) / factorial(i) 
                bandera = False
            else:
                result += pow(num, i) / factorial(i)
                bandera = True

    print('El valor de termino',termino ,'es:', result)



num1 = int(input('Ingrese un termino de la serie: '))
numF = int(input('Coseno de: '))
""" 
num2 = int(input('Ingrese la aproximacion de la serie hasta un n dado: '))
num3 = int(input('Ingrese la toleracia hasta donde llegara la serie: ')) """

coseno(numF, num1)
