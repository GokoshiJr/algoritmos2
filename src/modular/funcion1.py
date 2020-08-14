# 16. Evalúe la siguiente función matemática: f(a,b,c,d,e) = ((a! + b! + c!) / d!) + e^c / e!
# Ejemplo: Si a = 5, b = 1, c= 4 , d = 3, e = 2 → despliega: 32,17

def factorial(numero):
    fact = 1
    for i in range (1, numero+1):
        fact *= i
    return (fact)

def formula(a, b, c, d, e):
    termino1 = termino2 = result = 0
    termino1 = (factorial(a) + factorial(b) + factorial(c)) / factorial(d)
    termino2 = pow(e, c) / factorial(e)
    result = termino1 + termino2
    return (result)

a, b, c, d, e = 5, 1, 4, 3, 2
print('Despliega: {:.2f}'.format(formula(a, b, c, d, e)))
