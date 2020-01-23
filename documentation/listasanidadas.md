:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)


# 6. LISTAS ANIDADAS[ ]

Como ya dijimos podemos incluir listas dentro de otra lista

````python
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

r = [a,b,c]

print (r)
````
> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Si queremos acceder a cualquiera de estos números debemos acceder primero al _**primer índice**_
que correspondera a una de las 3 listas, y después a un _**segundo índice**_ que coresponderá a uno de los números
de la lista, lo vemos con un ejemplo.
````python
print(r[2][1])  # Primer índice[2]  corresponde al 3º grupo es decir a la lista "c"
                # y el segundo índice [1] al número 8
````
> 8
