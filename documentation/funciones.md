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

## Enviado Argumentos por ORDEN

````python
def resta(a,b): # Esta función recibirá 2 argumentos(1,2) e irán por ORDEN 1 será 'a' y 2 será 'b'
    return a-b

print(resta(1,2))
````
>-1

## Enviado Argumentos por NOMBRE

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

