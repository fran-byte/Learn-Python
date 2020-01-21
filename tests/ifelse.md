_[< Home >](../README.md)_ _[< Indice >](indicetests.md)_

# 2 - CONDICIONALES 
## if, elif, else
#### Ejercicio 1:
Pide al usuario que introduzca 3 números enteros.
Condicionamos de la siguiente forma:
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

###### if anidados

Realiza un ejercicio que te pida un número entre el 1 y el 5.
Ahora debes preguntar si el número 
Ahora ponemos las siguientes condiciones:
Que imprima el número mayor, Si no hay ninguno mayor a los otros 2 hazlo saber por pantalla.

````python
print("Piense un número de 1 a 4.")
print("Conteste S (sí) o N (no) a mis preguntas.")
primera = input("¿El número pensado es mayor que 2? ")
if primera == "S":
    segunda = input("¿El número pensado es mayor que 3? ")
    if segunda == "S":
        print("El número pensado es 4.")
    else:
        print("El número pensado es 3")
else:
    segunda = input("¿El número pensado es mayor que 1? ")
    if segunda == "S":
        print("El número pensado es 2.")
    else:
        print("El número pensado es 1.")
print("¡Hasta la próxima!")
````