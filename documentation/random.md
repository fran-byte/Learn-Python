:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 39. Módulo random


Este módulo contiene funciones para generar números aleatorios:


````python
import random

# Flotante aleatorio >= 0 y < 1.0
print(random.random())      

# Flotante aleatorio >= 1 y <10.0       
print(random.uniform(1,10))

# Entero aleatorio de 0 a 9, 10 excluído
print(random.randrange(10))

# Entero aleatorio de 0 a 100
print(random.randrange(0,101))

# Entero aleatorio de 0 a 100 cada 2 números, múltiples de 2
print(random.randrange(0,101,2))

# Entero aleatorio de 0 a 100 cada 5 números, múltiples de 5
print(random.randrange(0,101,5))
````
>0.12539542779843138
>6.272300429556777
>7
>14
>68
>25

## Muestras
También tiene funciones para tomar muestras:
````python
# Letra aleatoria
print(random.choice('Hola mundo'))

# Elemento aleatorio
random.choice([1,2,3,4,5])

# Dos elementos aleatorios
random.sample([1,2,3,4,5], 2)
````

> o
> 3
> [3, 4]

## Mezclas
Y para mezclar colecciones:
````python
# Barajar una lista, queda guardado
lista = [1,2,3,4,5]
random.shuffle(lista)
print(lista)
````
> [3, 4, 2, 5, 1]

