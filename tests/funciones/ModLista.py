# Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

# Borrar los elementos duplicados.
# Ordenar la lista de mayor a menor.
# Eliminar todos los números impares.
# Realizar una suma de todos los números que quedan.
# Añadir como primer elemento de la lista la suma realizada.
# Devolver la lista modificada.
# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista



lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modificar(l):
  c= set (l)  # pasamos la lista a un conjunto para eliminar los duplicados
  lista1 = list(c) # Y volvemos a convertirlo en una lista
  lista1.sort(reverse=True) # lo ordenamos de mayor a menor
  listaimpar = []

  for a in lista1:

    if a%2 != 0: # Solamente los impares
      listaimpar.append(a) # Lo metemos en la lista listaimpar
  suma = sum(listaimpar)   # Sumamos todos los elementos
  
  listaimpar.insert(0, suma) # Colocamos suma en la posición 0 de la lista

  return listaimpar

listaMod = modificar(lista)
print (listaMod)
print( listaMod[0] == sum(listaMod[1:]) ) # comparamos el primer elemento de listaMod, que es la suma del resto de elmentos
