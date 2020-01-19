## **Métodos (o funciones) para trabajar con las LISTAS en Python**


#### lista = **list()** 		 # Declaración de una lista


#### **len**(lista) 		# Cuenta el número de elementos de la lista


lista.**insert**(pos, x)    # Agrega un elemento (x) al final de la lista.


lista.**extend**(lista2)    # Une dos listas (une la lista2 (la que se pasa como parámetro) a la lista)


lista.**remove**(x)		 # Borra el primer elemento de la lista cuyo valor sea x. Sino existe devuelve un error


lista.**pop**(pos)		 # Borra el elemento en la posición dada de la lista, y lo devuelve.


**del** lista[:]		 # Borra todos los elementos de la lista (lista.clear())


lista.**index**(x)		 # Devuelve el índice en la lista del primer elemento cuyo valor sea x.


lista.**count**(x) 		 # Devuelve el número de veces que x aparece en la lista.


lista.**sort**(cmp=None, key=None, reverse=False) # Ordena los ítems de la lista


lista.**reverse**()		 # Invierte los elementos de la lista.


listaCopia = lista[:] # Devuelve una copia de la lista (lista.copy())

