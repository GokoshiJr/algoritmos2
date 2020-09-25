#!/usr/bin/env python3

def seleccion(stringArray: list) -> list:        
    for i in range (0, len(stringArray) - 1):
        minimo = i
        for j in range (i + 1, len(stringArray)):
            if stringArray[j].lower() < stringArray[minimo].lower():
                minimo = j
        temporal = stringArray[i]
        stringArray[i] = stringArray[minimo]
        stringArray[minimo] = temporal
    return stringArray

def mostrarStrings(stringArray: list):
    palabra = str
    for palabra in stringArray:
        print('\t{0}'.format(palabra.lower()))

if __name__ == "__main__":    
    try:
        palabras = ['luNES','marTes','Miercoles','Jueves','VIERNES','sabado','domingo']        
        mostrarStrings(seleccion(palabras))
    except:
        print('Error...')    
    