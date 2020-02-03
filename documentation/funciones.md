:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 17. FUNCIONES
## def nombre()

Son bloques de código a las que se les asocia un nombre, puede recibir o no argumentos como entrada, sigue una secuencia de sentencias realizando una tarea y se la puede llamar tantas veces como sea preciso.

En lugar de repetir bloques y bloques de código iguales o similares, creamos funciones que se ocuparan de esas tareas redundantes.


````python
def test(): # Esta función no recibirá ningún argumento.
    return "texto",20,[1,2,3]

print (test())
````
>('texto', 20, [1, 2, 3])

Los valores que se reciben se denominan parámetros, 
y durante la llamada los valores que se envían se denominan argumentos.

## Enviado Argumentos por POSICIÓN (orden)
Cuando enviamos argumentos a una función, estos se reciben por orden, (llamados argumentos por posición)


````python
def resta(a,b): # Esta función recibirá 2 argumentos(1,2) e irán por ORDEN 1 será 'a' y 2 será 'b'
    return a-b

print(resta(1,2))
````
>-1

## Enviado Argumentos por NOMBRE
Es posible cambiar este orden de los parámetros si 
indicamos durante la llamada que valor tiene cada parámetro a partir de su nombre.
````python
def resta(a,b): # Esta función recibirá 2 argumentos(1,2) e irán por NOMBRE 1 será 'a' y 2 será 'b'
    return a-b

print(resta(b=2,a=1))
````
>-1

## Envitando ERRORES en devoluciones

````python
def resta(a=None, b=None): # Declaramos estas variables directamente con None (vacías)
    if a==None or b==None:
        print("Error, envía 2 números a la función")
    else:
        return a-b
print(resta(1,2))
````

## Pasando Argumentos por VALOR
Estos números se pasan por VALOR y se crea una copia dentro de la función, 
por eso no les afecta externamente lo que hagamos con ellos:
````python
def doblar_valor(numero):
    numero *= 2 
    return numero
n = 10 # si colocamos aquí esta variable hará que lo que hagamos en la función no tendrá efecto
doblar_valor(n)
print(n) 
````
>10

## Si lo que deseamos es que nos "funcione" el paso por VALOR en una variable

````python
def doblar_valor(numero):
    return numero*2 # Pasamos el resultado y no la variable

n = 10 
n=doblar_valor(n)
print(n) 
````
>20

## Pasando Argumentos por REFERENCIA

Por otro lado las listas u otras colecciones, como son tipos compuestos se pasan por REFERENCIA, 
y aquí si las modificamos dentro de la función ahora si que se quedarán modificadas también fuera:

````python
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i]*=2 
ns=[10,50,100]
doblar_valores(ns)
print (ns)

````
>[20, 100, 200]



## También podemos CREAR una COPIA de la llamada para Evitar Modificaciones
````python
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i]*=2 
ns=[10,50,100]
doblar_valores(ns)
print (ns[:]) # no estamos enviado 'ns' si no una COPIA de 'ns'
````
