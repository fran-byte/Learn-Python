:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 40. Módulo math


Este módulo contiene un buen puñado de funciones para manejar números, hacer redondeos, sumatorios precisos, truncamientos... además de constantes.

## Redondeos
````python
import math

print(math.floor(3.99))  # Redondeo a la baja (suelo)
print(math.ceil(3.01))   # Redondeo al alta (techo)
````
>3
>4

## Sumatorio mejorado

````python
numeros = [0.9999999, 1, 2, 3])
math.fsum(numeros)
````

> 6.9999999

## Trucamiento

````python
math.trunc(123.45)
````
> 123

## Potencias y raices



````python
math.pow(2, 3)  # Potencia con flotante 
math.sqrt(9)    # Raíz cuadrada (square root)
````
>8.0

>3.0

## Constantes


````python
print(math.pi)  # Constante pi
print(math.e)   # Constante e
````
> 3.141592653589793
> 2.718281828459045
