class Vehiculo():

    def __init__(self, marca = '', modelo = ''):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True
    
    def acelerar(self): 
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print('\n Marca: {0} \n Modelo: {1} \n En Marcha: {2} \n Acelerando: {3} \n Frenando: {4}'.format(self.marca, self.modelo, self.enMarcha, self.acelera, self.frena))

# Para Heredar, le pasamos por parametro la clase padre a la clase hija
class Moto(Vehiculo):

    hCaballito = ''
    def caballito(self):
        self.hCaballito = 'Haciendo Caballitooo'

    # Sobre carga de metodos
    def estado(self):
        print('\n Marca: {0} \n Modelo: {1} \n En Marcha {2} \n Acelerando: {3} \n Frenando: {4} \n Caballito: {5} \n'.format(self.marca, self.modelo, self.enMarcha, self.acelera, self.frena, self.hCaballito))

class Furgoneta(Vehiculo):

    def carga(self, cargar: bool) -> str:
        self.cargado = cargar
        if(self.cargado):
            return ' La Furgoneta esta cargada'
        else:
            return ' La Furgoneta no esta cargada'

class VElectricos(Vehiculo):

    def __init__(self, marca: str, modelo: str):
        super().__init__(marca, modelo)
        self.duracion = 100
    
    def cargarEnergia(self):
        self.cargando = True

# -- Herencia Multiple --
# como hay 2 constructores, se le da prioridad al constructor 
# de la clase que este de primera en el parametro

class biciElectrica(VElectricos, Vehiculo):    
    pass

if __name__ == "__main__":
    import os
    os.system('clear') 

    moto = Moto('Yamaha', 'CBR')
    # moto.caballito()
    moto.estado()

    furgo = Furgoneta('Renault', 'Kangoo')
    furgo.arrancar()
    furgo.estado()
    print(furgo.carga(True))

    bici = biciElectrica('RX', 'Modelo A')
    bici.estado()
     