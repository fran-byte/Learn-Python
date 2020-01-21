_[< Home >](../README.md)_ _[< Indice >](indicetests.md)_

# 2 - CONDICIONALES 
## if, elif, else
#### Ejercicio 1:
Pide al usuario 3 números enteros.
Ahora ponemos las siguientes condiciones:
Que imprima el número mayor, Si no hay ninguno mayor a los otros 2 hazlo saber por pantalla.

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
    print ("No hay ningún nº mayor a los otros 2")
````