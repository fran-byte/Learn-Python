_[< Home >](../README.md)_ _[< Indice >](indicetests.md)_

# 1 - CONDICIONALES 
## if elif else
#### Ejercicio 5:
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