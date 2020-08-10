# 12. Leer 2 números que tengan más de 3 dígitos. Si el número de dígitos del primer número es impar, leer un dígito y adicionar al principio del mismo. Luego sume sus divisores de ambos números y determine si ambos tienen la misma suma de sus divisores o si el primer número tiene una mayor cantidad de  divisores que el segundo número, en ese caso saquen el mensaje “Sigan Adelante!!”, en caso contrario  despliegue: “Cuidado!”.  

def menu():
    print(" Menu Principal")
    print("1) Programa Adelante")        
    print("2) Salir")
    opcion = input("Seleccione una Opción:")
    print('')
    return opcion

def divisores(num):
    divisor = i = sumatoria = 0
    for i in range (1, num + 1):
        if(num % i == 0):
            divisor = i
            sumatoria = sumatoria + divisor            
    return sumatoria

def cantidadDig(num):
    contador = 0
    aux = num
    while(aux > 0):
        aux //= 10
        contador += 1
    return contador

def adelante(num1, num2):

    adicion = 0
    if(cantidadDig(num1) % 2 == 1):
        adicion = int(input('Adicione un digito al num1:'))
        num1 = (num1 * 10) + adicion
    
    if((divisores(num1) == divisores(num2)) | (divisores(num1) > divisores(num2))): 
        print('Sigan Adelante!!\n')
    else:
        print('Cuidado!\n')

salir = False
while not salir: 
    opcion = menu()
    if(opcion=="1"):
        num1 = int(input('Ingrese el numero1:'))
        num2 = int(input('Ingrese el numero2:'))
        if((cantidadDig(num1) > 3) & (cantidadDig(num2) > 3)):
            adelante(num1, num2)
        else:
            print('Error, ambos numeros deben tener mas de 3 cifras')
    elif(opcion == "2"):
     salir = True
    else:
        print("Debe ser un numero del 1 al 2")       
