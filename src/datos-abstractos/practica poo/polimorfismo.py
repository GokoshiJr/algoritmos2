class Coche():

    def desplazamiento(self):
        print('\n Me desplazo usando 4 ruedas')

class Moto():
    def desplazamiento(self):
        print('\n Me desplazo usando 2 ruedas')

class Camion():
    def desplazamiento(self):
        print('\n Me desplazo usando 6 ruedas')

def desplazamientoVehiculo(vehiculo):
    # Polimorfismo
    vehiculo.desplazamiento()
    
if __name__ == "__main__":
    import os
    os.system('clear')

    carro1 = Coche()
    desplazamientoVehiculo(carro1)

    