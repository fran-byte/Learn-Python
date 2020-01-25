:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)


# 9. for 
## Recorriendo LISTAS

En Pyton **for** se utiliza muy a menudo para recorrer el contenido de las listas, tuplas, diccionarios, etc...
Podriamos hacerlo con **while** pero la líneas de código serían mayores

````python
ns = [1,2,3,4,"CINCO",6,7,"OCHO",9]
for numero in ns:   # Vamos a ir pasandole el contenido de cada indice de (ns) a (numero) y no finalizará hasta recorrerlo entero
                    # este indice de (ns) se irá incrementando automáticamente.
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
