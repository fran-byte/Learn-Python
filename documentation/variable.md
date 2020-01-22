
:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)




# 2- VARIABLES y TIPOS de DATOS

## Definiendo una variable

En Python las variables se crean al definirse por primera vez.
Puede almacenar texto, números o estructuras más complejas.
Es recomendable que el nombre de la variable tenga relación con lo que se va a almacenar en ella.
No pueden empezar con ningún número 

````python
saludio1= "Buenos días" # (esto es un comentario en Phyton, utilizaremos el simbolo: # y después el texto)
````
### Empezaremos con los tipos que existen, aunque profundizaremos más adelante en cada uno de ellos:
## Tipo de Cadenas
Son texto entre comillas (simples o dobles) y admiten operadores.
````python
cadena1 = ("comillas dobles")
cadena2 = ('comillas simples')

a = "Buenos"
b = "días !"
sumaCadenas = a + " " + b
print (sumaCadenas)
````
## Tipos de booleanos
Solo puede admitir Verdadero o Falso. Usados en condiciones y bucles, que veremos más adelante.
True / False
````python
a = 5
print(a==5) # Le estamos diciendo que imprima por pantalla la condición de esa igualdad y nos devolvera:
True
````



## Tipos de Enteros
### Numeros:

Enteros: Son los Números que carecen de decimales
**int** (entero) o **long** (entero largo para más precisión).
`````python
edad = 25
`````
Reales: Son los números que tienen decimales y son del tipo float.
`````python
longitud = 25.638
`````
Complejos: Números que tienen una parte real y una imaginaria. Estos números se denominan complex.
`````python
n = X= 3,8 + 9j
`````

 

## Tipos de conjuntos
Colección de datos sin elementos repetidos, desordenados y separadas por comas, entre llaves.
`````python
conjunto = {'casa', 'arbol', 'perro',356,'empanadilla',-89,'mango', 'quesito'}
`````

## Tipos de listas
Son listas que almacenan vectores (es decir arrays) y pueden contener tipos de datos diferentes. 
`````python
lista1 = ['17',-66,99,44,"adios", 'hola',6,7,"8",9,10,11,12,13]
lista2 = lista1[0:8:2] # Cogemos de la lista1 desde la posición 0 a la 8 y de 2 2n 2; y lo metemos en la lista2
print(lista2)
['17', 99, 'adios', 6] 
`````
 

## Tipos de tuplas:
Es una lista **inmutable**
`````python
tupla1 = ("pajaro",34,"9",reloj)
`````

## Tipos de diccionarios:
Podemos almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones.
Y podemos identificar cada elemento por una clave (Key).
`````python
diccionario1 = {'coche' : 'Mercedes', 'Color' : 'rojo', 'velocidad': 280 }
print (diccionario1['coche']) # Al introduccir la clave "coche" Obtendremos "Mercedes"
`````