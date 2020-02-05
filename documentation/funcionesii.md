:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 18. FUNCIONES II
En ocasiones no conocemos el número de elementos que vamos a enviar a una función.

Para estos casos utilizaremos los parámetros indeterminados por posición y por nombre.

## Argumentos INDETERMINADOS por POSICIÓN y NOMBRE
## por POSICIÓN

Para recibir un número indeterminado de parámetros por posición,

debemos crear una lista dinámica de argumentos (una tupla en realidad) definiendo el parámetro con un asterisco:

````python
def indet_pos(*args): ## (args) no es una palabra reservada, pero cuando usamos argumentos sí que la ponemos
    for arg in args:
        print(arg)

indet_pos(5,"Hola",[1,2,3,4,5])
````
>5  
Hola  
[1, 2, 3, 4, 5]
