# 15. .Leer tres números mayores a cero y encuentre su máximo común. Ejemplo: Si A = 24, B = 12 y C = 18 → El mcd es: 6. 

def divisores2(num1, num2, num3):
    mcd = 1
    contador = 2
    while ((contador <= num1) & (contador <= num2) & (contador <= num3)):
        while ((num1 % contador == 0) & (num2 % contador == 0) & (num3 % contador == 0)):
            mcd *= contador
            num1 //= contador
            num2 //= contador
            num3 //= contador
        contador += 1
    return (mcd)

print('El mcd es {}'.format(divisores2(24, 12, 36)))
    