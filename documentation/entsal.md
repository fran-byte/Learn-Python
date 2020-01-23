
:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)




# 3- ENTRADAS y SALIDAS

## print()

Esta función nos permite mostrar texto por pantalla,
el argumento de la función irá entre paréntesis, y puede ser un texto entre comillas simples o dobles o una variable.

````python
print ("Hello World")
x = 5
print (x)

````
> Hello World
>
> 5
````python
print (""" Con estas 3 comillas con
un ENTER podemos cambiar 
de línea las veces que queramos y así 
no tenemos que colocar varios print.""")
````
> Con estas 3 comillas con  
un ENTER podemos cambiar  
de línea las veces que queramos y así  
no tenemos que colocar varios print.

Pera Si queremos incluir comillas dentro de comillas, lo hacemos con una contrabarra ( \\ )
````python

print ("Esta contrabanda no saldrá pero deja en crudo el siguiente caracter \" que son estas comillas \"")
````
> Esta contrabanda no saldrá pero deja en crudo el siguiente caracter " que son estas comillas "    
---
````python
print ("Podemos utilizar\nPara hacer un salto de línea, o un\tpara una tabulación")
````
> Podemos utilizar
> Para hacer un salto de línea, o un    para una tabulación