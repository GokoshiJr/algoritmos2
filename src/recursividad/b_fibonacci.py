# 1. Escriba una definición recursiva de una función que tiene un parámetro n de tipo entero y que
# devuelve el n-ésimo número de Fibonacci. Los números de Fibonacci se definen de la siguiente
# manera: F0=1 F1=1 Fi+2=Fi + Fi+1

def fibonacci(num):
    if (num <= 2):
        return 1
    else:
        return (fibonacci(num - 2) + fibonacci(num - 1))

print(fibonacci(10))
