# 17. Generar los n primeros términos de la siguientes series:
# a) 1, 10, 1 20, 2, 30, 2, 40, 3, 50, 3, 60, 4,...
# b) 2, 2, 3. 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6,... 

def serie1(tope):
    j = 0
    i = 1
    while (i < tope):
        if (i % 2 == 1):
            j += 1        
        print(j, end = ', ')
        print(i * 10, end = ', ')
        i += 1
    print('')
serie1(8)

def serie2(tope):
    i = j = 0
    while (i < tope):
        for j in range (1, i + 1):
            if (i > 1):
                print(i, end = ', ')
        i += 1
    print('')

serie2(8) 
