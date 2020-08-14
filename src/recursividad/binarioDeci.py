# 8. Programe un método recursivo que transforme un número expresado en notación binaria a un
# número entero.

def binarioDeci(num):
    if (num < 10):
        return (num)
    else:
        return ((num % 10) + (binarioDeci(num // 10) * 2))

print(binarioDeci(10101))
