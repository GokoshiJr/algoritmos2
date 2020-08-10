# 9. Anexar un dígito a un número dado por adelante. Ej.: Si N = 123 y Dig = 7 → N = 7123

def anexar(base, anexo):
    temp = base
    digito = contador = 0
    while(temp > 0):        
        contador += 1
        temp //= 10        
    digito = (anexo * pow(10,contador)) + base    
    print(digito)

anexar(123, 7)  
  