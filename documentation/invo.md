:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 20. INVOCANDO EXCEPCIONES

Podemos llamar un error manualmente.
````python
def funcion_error(algo=None):
    if algo is None:
        print("Error! No se permite un valor nulo (con un print)")

funcion_error()
````

## raise

Gracias a raise podemos lanzar un error manual pasándole el identificador.
Luego simplemente podemos añadir un except para tratar esta excepción que hemos lanzado:

````python
def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("Error! No se permite un valor nulo")
    except ValueError:
        print("Error! No se permite un valor nulo (desde la excepción)")

mi_funcion()
````
>Error! No se permite un valor nulo (desde la excepción)