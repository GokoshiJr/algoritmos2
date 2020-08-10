# 11. Leer 4 números que sean mayores a cero y determine si son o no amigos. 
# Un número es amigo del otro, si al sumar todos los dígitos
#  de cada número es el mismo que el de los otros.
# Ejemplo: Si A = 324, B = 225 C = 81 y D = 153 → “Son Amigos” 

def amigos(num1, num2, num3, num4):
    s1 = s2 = s3 = s4 = 0
    s1 = sumaDigitos(num1)
    s2 = sumaDigitos(num2)
    s3 = sumaDigitos(num3)
    s4 = sumaDigitos(num4)
    if((num1 > 0) & (num2 > 0) & (num3 > 0) & (num4 > 0)):
        if(s1 == s2 & s1 == s3 & s1 == s4 & s2 == s3 & s2 == s4 & s3 == s4):
            print('Son amigos')
        else:
            print('No son amigos')
    else:
        print('No se puede realizar la operacion, todos los numeros deben ser mayores a 0.')     

def sumaDigitos(num):
    digito = aux = suma = int(0)
    aux = num
    while(aux > 0):
        digito = aux % 10
        suma = suma + digito
        aux //= 10
    return suma

num1, num2, num3, num4 = 324, 225, 81, 153
amigos(num1, num2, num3, num4)
