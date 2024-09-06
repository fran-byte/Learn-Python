:page_with_curl: [README](../README.md)  :pencil: [Ejercicios](/tests/indicetests.md)

# 9. for 
## Recorriendo LISTAS

En Pyton **for** se utiliza muy amenudo para recorrer el contenido de las listas, tuplas, diccionarios, etc...
Podríamos hacerlo con **while** pero las líneas de código serían mayores

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

## ITERANDO (recorriendo) con zip

Si queremos recorrer o iterar dos listas a la vez, lo podemos conseguir mediante la función zip (cremallera) y ayudandonos de un contador

````python
lista1 = [1,"DOS",3,"CUATRO",5,"SEIS",7,"OCHO",9]
lista2 = ["UNO",2,"TRES",4,"CINCO",6,"SIETE",8,"NUEVE"]
contador=0
for i,a in zip(lista1,lista2): # Cada lista irá volcandose en (i) y (a) respectivamente
                 
    print(lista1[contador],lista2[contador]) 
    contador+=1 # Vamos incrementando el (contador) que será nuestro índice para ir recorriendo las listas e imprimiendo
````

>1 UNO

>DOS 2

>3 TRES

>CUATRO 4

>5 CINCO

>SEIS 6

>7 SIETE

>OCHO 8

>9 NUEVE

El único inconveniente es que ambas listas deben de tener el mismo número de elementos
