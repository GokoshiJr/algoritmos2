def factorial(num):
    if (num == 0): # Caso base
        return 1
    else: # Caso general
        return (num * factorial(num - 1))

# n >= 0
n = 5
print(factorial(n))
