_[< Home >](../README.md)_ _[< Indice >](indicetests.md)_

# 1 - Básicos
#### Ejercicio 1:

Escribe un programa que **muestre** por pantalla el texto **Hello Word!**

````python
print("Hello Word!")
````

Hello Word!

#### Ejercicio 2:

Escribe un programa que pida al usuario **introducir** una cadena y la almacene en una variable y luego muestre por pantalla 
el contenido de la variable.

````python
cadena = input("Introduce una cadena de texto: ")
print(cadena)
````

#### Ejercicio 3:
Escribir un programa que calcule el [volumen](https://es.wikipedia.org/wiki/Esfera) de una balón pidiendo por teclado al usuario los datos necesarios al usuario.

````python
radio = float(input("Radio: "))
PI = 3.14159265359
print("El volumen es : ",(4*PI*radio**3)/3)
````

#### Ejercicio 4:
Crea una función que nos devuelva por pantalla el número mayor de 3 números enteros. Llámalos directamente desde un input masivo. Si no hay ninguno mayor a los otros 2 hazlo saber por pantalla. (Utiliza los condicionales)

````python
def n_Max (a, b, c):
    if a > b and a > c:
        return print (a)
    elif b > a and b > c:
        return print (b)
    elif c > a and c > b:
        return print (c)
    else:
        return print ("No hay ningún nº mayor a los otros 2")

a = int(input("nº1: "))
b = int(input("nº2: "))
c = int(input("nº3: "))


n_Max(a,b,c)
````