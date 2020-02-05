:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 18. FUNCIONES II
En ocasiones no conocemos el número de elementos que vamos a enviar a una función.

Para estos casos utilizaremos los parámetros indeterminados por posición y por nombre.

## Argumentos INDETERMINADOS por POSICIÓN 

Recibiendo parametros indeterminados por posición,

Envíamos una lista dínámica, una tupla realmente, y para eso definimos el parámetro con un asterisco:

````python
def indet_pos(*args): ## (args) no es una palabra reservada, pero se usan por convención
    for arg in args:
        print(arg)

indet_pos("Phyton","Hola",3,[5,53,21,5])
````
>Phyton  
Hola  
3  
>[5, 53, 21, 5]
## Argumentos INDETERMINADOS por NOMBRE (o Clave)
Recibiendo parámetros por nombre (keyword args)

Evidentemente tenemos que crear un diccionario dinámico con estos argumentos y para ello definimos el parámetro con dos asteriscos:

````python
def indet_word(**kwargs): ## (kwargs) no es una palabra reservada, pero se usa por convención.
    print(kwargs)

indet_word(m="Python", b="Hola", n=3, s=[1,2,3,4,5]) 
````
>{'m': 'Python', 'b': 'Hola', 'n': 3, 's': [1, 2, 3, 4, 5]}

## Por Nombre y Posición

Recibiendo de ambos tipos, para ello tenemos que crear 2 colecciones dinámicas.

Enviamos primero los argumentos indet. por valor y luego los de clave/valor:

````python
def indet_mix(*args,**kwargs):
    multiplicando = 1
    for arg in args:
        multiplicando*= arg
    print("resultado = ", multiplicando)
    for kwarg in kwargs:
        print(kwarg, "=", kwargs[kwarg])

indet_mix(3, 6, 8, name="Fran", age=22)
````
>resultado =  144  
name = Fran  
age = 22
>