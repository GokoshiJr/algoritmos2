# 7. Programe un método recursivo que transforme un número entero positivo a notación binaria. 

def deciBinario(num):
    if (num < 2):
        return (num)
    else:
        return ((10 * deciBinario(num // 2)) + (num % 2))

print(deciBinario(20))
