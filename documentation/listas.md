:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)


# 5. LISTAS [ ]

Pueden ser cadenas de texto, caracteres, otras listas, van entre corchetes [ ] y son MODIFICABLES

````python
lista1 = ["Python",1,2,"3",[4,5,"seis"],7,8] # Podemos observar otra lista entre corchetes dentro de la lista1
print (lista1)
````

>['Python', 1, 2, '3', [4, 5, 'seis'], 7, 8]
>
Podemos hacer **_Slicing_** también con las listas:
````python
print (lista1[2:6])
````
>[2, '3', [4, 5, 'seis'], 7]
>
Modificarlas.
````python
lista1[3]="TRES"
print (lista1)
````
>['Python', 1, 2, 'TRES', [4, 5, 'seis'], 7, 8]

Utilizando la función **_len_** podremos saber la longitud de esa lista.
````python
print (len(lista1))

````
>7
>
>
Las siguientes funciones las iremos utilizando según vayamos avanzado...

##  Métodos (o funciones) para trabajar con las LISTAS en Python


lista = **list()** 		 # Declaración de una lista


**len**(lista) 		# Cuenta el número de elementos de la lista


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


