# 2. La forma para calcular cuantas maneras diferentes tengo para elegir r cosas distintas de un
# conjunto de n cosas es:
# C(n,r) = n! / (r!*(n-r)!)
#
# Donde la función factorial se define como
# n! = n *(n-1)*(n-2)*…*2*1
#
# Descubra una versión recursiva de la fórmula anterior y escriba una función recursiva que calcule el
# valor de dicha fórmula.  

def elegir(n, r):
    if ((r == 0) | (n == r)):
        return (1)
    elif (r > n):
        return (0)    
    else:        
        return (elegir(n - 1, r - 1) + elegir(n - 1, r)) 

print(elegir(5, 2))

