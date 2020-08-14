# 11. Cuál es el resultado de esta función para distintos valores de X?
# Static int f(int x) {
#  if (x >100) {
#  return (x-10);
#  }
#  else {
#  return(f(f(x+11)));
#   }
# }

def funcion(num):
    if (num > 100):
        return (num - 10)
    else:
        return funcion(funcion(num + 11))

print(funcion(300))

# para las x < 100 = 91
# para las x > 100 = x - 10