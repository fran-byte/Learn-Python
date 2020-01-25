:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/índicedocu.md) :pencil: [Ejercicios](/tests/índicetests.md)


# 9. for 
## Recorriendo LISTAS

En Pyton **for** se utiliza muy a menudo para recorrer el contenido de las listas, tuplas, diccionarios, etc...
Podriamos hacerlo con **while** pero la líneas de código serían mayores

````python
ns = [1,2,3,4,"CINCO",6,7,"OCHO",9]
for numero in ns:   # Vamos a ir pasandole el contenido de cada índice de (ns) a (numero) y no finalizará hasta recorrerlo entero
                    # este índice de (ns) se irá incrementando automáticamente.
    print(numero) 
````

>1  
>2  
>3   
>4  
>CINCO  
>6  
>7  
>OCHO  
>9  

## Recorriendo LISTAS y MODIFICANDOLAS
## in enumerate()


````python
ns = [1,2,3,4,5,6,7,8,9]
for indice,numero in enumerate(ns):   # El contenido de (ns) a (numero) y el índice numérico a (indice) (RECORRIENDO LA LISTA)
    ns[indice]*=10 # Multiplicación en asignación (MODIFICANDO LA LISTA)             
    print(ns[indice]) 
````
Vease que **enumerate**(ns) nos de vuelve 2 valores, uno es nº de registro o índice y otro es el contenido de ese índice,
 el índice se quedará en la variable (indice) que hemos creado en el propio (for) y el contenido de ese índice se irá a (numero)

Puede parecer algo confuso al principio pero según vayamos haciendo ejercicios nos resultará muy fácil...