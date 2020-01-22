
:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)




# 2- VARIABLES y TIPOS de DATOS

## Definiendo una variable

En Python las variables se crean al definirse por primera vez.
Puede almacenar texto, números o estructuras más complejas.
Es recomendable que el nombre de la variable tenga relación con lo que se va a almacenar en ella.
No pueden empezar con ningún número.

## Palabras reservadas en Python

No se pueden utilizar para nombrar variables:
| and | as | assert | async | await | break |
| --- | --- | --- | --- | --- | --- |
| : continue | : def | : del | : elif | : else | : except |
| : false | : finally | : for | : from | : global | : if |
| : import | : in | : is | : lambda | : none | : nonlocal |
| : not | : or | : pass | : raise | : return |: true |
| : try | : while | : with | : yield | :  | :  |








````python
saludio1= "Buenos días" # (esto es un comentario en Phyton, utilizaremos el simbolo: # y después el texto)
````
### Empezaremos con los tipos que existen, 
(Aunque profundizaremos más adelante en cada uno de ellos)
## Tipo. Cadenas (str) o Strings  ""
Son texto entre comillas (simples o dobles) y admiten operadores.
````python
cadena1 = "comillas dobles"
cadena2 = 'comillas simples'

a = "Buenos"
b = "días !"
sumaCadenas = a + " " + b
print (sumaCadenas)
````
## Tipo. Booleanos
Solo puede admitir Verdadero o Falso. Usados en condiciones y bucles, que veremos más adelante.
True / False
````python
a = 5
print(a==5) # Le estamos diciendo que imprima por pantalla la condición de esa igualdad y nos devolvera:
True
````



## Tipo. Numeros
### Enteros:

Son los Números que carecen de decimales
**int** (entero) o **long** (entero largo para más precisión).
`````python
edad = 25
`````
### Reales: 

Son los números que tienen decimales y son del tipo float.
`````python
longitud = 25.638
`````
### Complejos:

Números que tienen una parte real y una imaginaria. Estos números se denominan complex.
`````python
n = 3,8 + 9j
`````

 

## Tipo. Conjuntos {}
Colección de datos sin elementos repetidos, desordenados y separadas por comas, entre llaves.
`````python
conjunto = {'casa', 'arbol', 'perro',356,'empanadilla',-89,'mango', 'quesito'}
`````

## Tipos. Listas [ ]
Son conjuntos ordenados de elementos pueden almacenar números, cadenas, otras listas...
Se colocan entre ([ ]) y los elementos van separados por comas.

`````python
lista1 = ['17',-66,99,44,"adios", 'hola',6,7,"8",9,10,11,12,13]
lista2 = lista1[0:8:2] # Cogemos de la lista1 desde la posición 0 a la 8 y de 2 2n 2; y lo metemos en la lista2
print(lista2)
['17', 99, 'adios', 6] 
`````
 

## Tipo. Tuplas ()
Es una lista **inmutable**
`````python
tupla1 = ("pajaro",34,"9",reloj)
`````

## Tipos. Diccionarios { : }
Podemos almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones.
Y podemos identificar cada elemento por una clave (Key).
`````python
diccionario1 = {'coche' : 'Mercedes', 'Color' : 'rojo', 'velocidad': 280 }
print (diccionario1['coche']) # Al introduccir la clave "coche" Obtendremos "Mercedes"
`````