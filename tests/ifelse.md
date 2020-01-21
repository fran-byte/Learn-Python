:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)


# 2 - CONDICIONALES 
## if, elif, else
#### Ejercicio 1:
Realiza un ejercicio que pida al usuario que introduzca 3 números enteros.
Debe imprimir el número mayor, Si no hay ninguno mayor a los otros 2 hazlo saber por pantalla.

````python
a = int(input("nº1: "))
b = int(input("nº2: "))
c = int(input("nº3: "))

if a > b and a > c:
    print (a)
elif b > a and b > c:
    print (b)
elif c > a and c > b:
    print (c)
else:
    print ("No hay ningún número que sea mayor a los otros 2")
````

#### Ejercicio 2:


Realiza un ejercicio que pida al usuario dos números, los compare e imprima cual de ellos es el mayor y cual es el menor o si son iguales.
Usa alguno de los condicionales de forma anidada.

````python
x = float(input("Introduzca un número: "))
y = float(input("Introduzca otro número: "))

if x == y:
    print (x, "y", y, "son iguales")
else:
    if x > y:
        print (x, "es mayor que", y)
    else:
        print (x, "es menor que", y)
````
