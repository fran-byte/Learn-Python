
:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)




# 3- ENTRADAS y SALIDAS

## print()

Esta función nos permite _**mostrar**_ texto por pantalla,
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
print (""" Con estas 3 comillas y con
un ENTER por línea podemos cambiar 
de línea las veces que queramos y así 
no tenemos que colocar varios print.""")
````
> Con estas 3 comillas y con
un ENTER por línea podemos cambiar  
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
>
> Para hacer un salto de línea, o un____para una tabulación



## input()

Esta función nos permite recoger **_texto_** por pantalla,
el argumento de la función irá entre paréntesis, y puede ser un texto entre comillas simples o dobles.
Lo podemos recoger en una variable.


````python
 texto1 = input("Entrada de texto: ")
````
### Conversión de Tipos:
También podemos hacer que el texto de la entrada se convierta a números enteros o flotantes y así poder operar con ellos.
````python
numeroEntero = int (input ("Introduce un número: "))
print(numeroEntero+50)

numeroDecimal = float (input ("Introduce un número decimal: "))
print(numeroDecimal+50)
````
