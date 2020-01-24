:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)


# 6. LISTAS ANIDADAS[ ]

Como ya dijimos anteriormente podemos incluir listas dentro de otra lista

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
print(r[2][1])  # Primer índice[2]  corresponde al 3º grupo es decir a la lista "c" ya anidada dentro de "r"
                # y el segundo índice [1] al número 8 (siempre empezamos a contar desde el índice 0)
````
> 8

### Modificando LISTAS ANIDADAS
En el ejemplo anterior, vamos a sumar los 2 primeros índices de las listas(anidadas) que hemos introducido y dejarlo en el tercer índice.

````python
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

r = [a,b,c]
r[0][2] = sum (r[0][:2]) # Estamos sumando del indice [0] (es decir la antigua lista "a" ahora anidada en "r")
                        # desde [:2] el índice 0 ya que no hemos puesto inicio alguno hasta el índice 2 (recordemos que este último no se toma)

r[1][2] = sum (r[1][:2]) # Hacemos lo propio con el rsto de índices
r[2][2] = sum (r[2][:2]) 
print (r)
````
