# Se desea eliminar todos los numeros duplicados de una lista o vector
# Por ejemplo si toma los valores [4,7,11,4,9,5,11,7,3,5]
# Ha de cambiarse a [4,7,11,9,5,3]

def eliminar(numArray: list) -> list:
  largo = len(numArray)
  unicos = list()
  for i in range ((largo - 1), -1, -1):
    if (numArray[i] not in unicos):
      unicos.append(numArray[i])
    else:
      numArray.remove(numArray[i])
  return numArray

if __name__ == "__main__":
  numeros = [4, 7, 11, 4, 9, 5, 11, 7, 3, 5]
  print(eliminar(numeros))
