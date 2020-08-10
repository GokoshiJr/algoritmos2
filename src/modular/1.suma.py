# 1. Sumar todos los dígitos de un número mayor a cero. Ejemplo: Si n = 57 → se devuelve 12

numero = temporal = digito = suma = 0

print("-" * 30)
print(" Suma de digitos")
print("-" * 30)

num = int(input(" Ingrese un número: "))
temp = num
print("-" * 30)
print(" Digitos Obtenidos:")

while (temp != 0):    
    dig = temp % 10 # Obtenemos un digito
    print(" ", dig) # Lo mostramos por consola
    suma += dig     # Lo acumulamos en suma
    temp = temp // 10

print("-" * 30)
print(" Suma de:", num, "es:", suma)
print("-" * 30)
print(" Fin del programa")
