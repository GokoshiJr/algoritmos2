class Persona():

    def __init__(self, nombre = '', edad = 0, lugarResidencia = ''):
        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia = lugarResidencia

    def descripcion(self):
        print('\n Nombre: {} \n Edad: {} \n Residencia: {}'.format(self.nombre, self.edad, self.lugarResidencia))

class Empleado(Persona):

    # Al disenar la herencia
    # Preguntarnos siempre el principio de sustitucion    
    # un 'Empleado' es siempre una 'Persona'
    # una 'Persona' no siempre es un 'Empleado'

    def __init__(self, salario: int, antiguedad: int, nombreEmpleado: str, edadEmpleado: int, residenciaEmpleado: str):
        # Llamamos al constructor de la clase Padre
        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print(' Salario: {} \n Antiguedad: {}'.format(self.salario, self.antiguedad))

julio = Empleado(1500, 15, 'Julio', 20, 'San Diego')
julio.descripcion()

andres = Persona('Andres', 12, 'San Diego')
andres.descripcion()

print(isinstance(andres, Empleado))
print(isinstance(andres, Persona))
