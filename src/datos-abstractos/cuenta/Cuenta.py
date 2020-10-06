class Cuenta():
    def __init__(self, titular: str, cantidad = 0.0):
        self.__titular = titular
        if (cantidad <= 0.0):
            self.__cantidad = 0
        else:
            self.__cantidad = cantidad
            
    def getTitular(self):
        return self.__titular

    def getCantidad(self):
        return self.__cantidad

    def setTitular(self, titular: str):
        self.__titular = titular

    def setCantidad(self, cantidad: float):
        self.__cantidad = cantidad

    def ingresar(self, cantidad: float) -> None:
        if (cantidad > 0):
            self.__cantidad += cantidad
    
    def retirar(self, retiro: float):
        if (self.__cantidad > retiro):
            self.__cantidad -= retiro
        else:
            self.__cantidad = 0

    def toString(self) -> str:
        return ' Titular: {} \n Monto Actual: {} \n'.format(self.__titular, self.__cantidad)

if __name__ == "__main__":    
    
    cuenta1 = Cuenta('Julio', 1500)    
    cuenta2 = Cuenta('Maria')

    cuenta1.retirar(500)

    cuenta1.ingresar(250)
    cuenta2.ingresar(300)

    print(cuenta1.toString())
    print(cuenta2.toString())
    