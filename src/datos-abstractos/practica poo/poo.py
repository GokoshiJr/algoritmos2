#!/usr/bin/env python3
class persona:   
    def __init__(self, nombre, edad = 20):
        self.nombre = nombre
        self.edad = edad    

class Carro():

    # Constructor
    def __init__(self):
        # encapsulamiento con __ en el nombre del campo de clase
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 
        self.__enMarcha = False
    
    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if (self.__enMarcha):
            chequeo = self.__chequeo()

        if (self.__enMarcha and chequeo):
            return 'El carro esta en marcha'
        elif (self.__enMarcha and chequeo == False):
            return 'Algo ha ido mal en el chequeo, no podemos arrancar'
        else:
            return 'El carro esta parado'

    def estado(self):
        print('El carro tiene {0} ruedas. Un ancho de {1} cm y un largo de {2}'.format(self.__ruedas, self.__anchoChasis, self.__largoChasis))

    # Metodo encapsulado - privado
    def __chequeo(self):
        print('Realizando chequeo interno')
        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'

        if (self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas'):
            return True
        else:
            return False

if __name__ == "__main__":
    aveo = Carro()
    print(aveo.arrancar(True))    
    aveo.estado()