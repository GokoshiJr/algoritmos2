# 13. Diseñe e implemente un algoritmo que imprima todas las posibles descomposiciones de un número natural como suma de números menores que él.
# 1 = 1
# 2 = 1+1
# 3 = 2 + 1
# 3 = 1+1+1
# 4 = 3+1
# 4 = 2+1+1
# 4 = 1+1+1+1
# 4 = 2+2
# N = (n-1) +1
# N = (n-2) + 2 = (n-2) + 1 + 1 

def descomposicion(num: int) -> str:
    if (num == 0):
        return
    if (num == 1):
        return ('1') 
    elif (num > 2):
        if (num > 3):
            return ("%s + %s" % (descomposicion(num - 3) , str(3)))        
        return ("%s + %s" % (descomposicion(num - 2) , "2"))
    else:
        return ("%s + %s" % (descomposicion(num - 1) , "1"))

print(descomposicion(1))
print(descomposicion(2))
print(descomposicion(3))
print(descomposicion(4))
