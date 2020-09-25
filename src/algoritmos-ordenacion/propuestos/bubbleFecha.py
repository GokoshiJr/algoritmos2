#!/usr/bin/env python3

"""
Run:
>>> python3 bubbleFecha.py
or
>>> bubbleFecha.py

Ejemplo:
>>> Cantidad de fechas a ordenar: 3
>>> Ingrese dia,mes,year (fecha 1): 12,08,1999
>>> Ingrese dia,mes,year (fecha 2): 25,05,1987
>>> Ingrese dia,mes,year (fecha 3): 04,12,2015
>>> [[25,05,1987], [12,08,1999], [04,12,2015]]
"""

def bubbleFechas(datesUnsorted: list) -> list:
    aux = []    
    a = datesUnsorted
    for i in range (len(a), 0, -1):
        for j in range(1, i):
            if( (a[j-1][2] > a[j][2]) or (a[j-1][2] == a[j][2] and 
                 a[j-1][1] > a[j][1]) or (a[j-1][2] == a[j][2] and 
                 a[j-1][1] == a[j][1] and a[j-1][0] > a[j][0]) ):
                aux = a[j]
                a[j] = a[j-1]
                a[j-1] = aux            
    return a

def cargarFechas() -> list:
    cantidad = int(input('\tCantidad de fechas a ordenar: '))
    fechaArray = []
    fecha = []
    for i in range (0, cantidad):
        userInput = input('\tIngrese dia,mes,year (fecha {}): '.format(i + 1))
        fecha = [int(numero) for numero in userInput.split(',')]
        fechaArray.append(fecha)
    return fechaArray

if __name__ == "__main__":    
    try:
        fechasCargadas = cargarFechas()
        fechasOrdenadas = bubbleFechas(fechasCargadas[:])
        print('\t{0}'.format(fechasOrdenadas))        
    except:
        print('\tError en la carga...') 
