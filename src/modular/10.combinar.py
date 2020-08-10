# 10. Leer dos números que tengan más de dos dígitos y combinarlos en un nuevo número.
#  Ej.: Si a = 23 y b = 6451 → el nuevo número que se devuelve es: c = 263451.

import random

def combinar(num1, num2):
    if ((num1 > 9) & (num2 > 9)):
        list1 = cargarLista(num1)
        list2 = cargarLista(num2)    
        print(toNum(combinarLista(list1, list2)))
    else:
        print('No se puede realizar la operacion debe ingresar numero de 2 digitos.')

def cargarLista(num):
    lista = []
    aux = num
    result = digito = 0    
    while (aux > 0):
        digito = aux % 10    
        result = (result * 10) + digito     
        aux //= 10
        lista.append(digito)  
    return (lista)

def combinarLista(list1, list2):
    universal = []
    ran = random.randint(1,2)
    if (ran % 2 == 0):        
        general = list2[:len(list2)//2] + list1[:len(list1)//2] + list2[(len(list2)//2):] + list1[(len(list1)//2):]
    else:
        general = list1[:len(list1)//2] + list2[:len(list2)//2] + list1[(len(list1)//2):] + list2[(len(list2)//2):]
    for i in range (len(general)):
        universal.append(general[i])
    return (universal)

def toNum(lista):
    num = 0
    for i in range (len(lista)):
        num = (num * 10) + lista[i]
    return (num)

num1 = int(input('Ingrese A:'))
num2 = int(input('Ingrese B:'))
combinar(num1, num2)
