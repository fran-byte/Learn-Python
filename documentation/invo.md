:page_with_curl: [README](../README.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 24. INVOCANDO EXCEPCIONES

Podemos llamar un error manualmente.
````python
def funcion_error(algo=None):
    if algo is None:
        print("Error! No se permite un valor nulo (con un print)")

funcion_error()
````

## raise

En ciertas ocasiones es posible identificar una situación en la que cierta condición provocará un error. En ese caso se puede levantar una excepción antes de que el error ocurra y emitir un mensaje correspondiente.

La expresión raise se utiliza para levantar excepciones definidas por el programador

````python
def levanta_excepcion(numero):
    """ Levantará una excepción con un mensaje propio en caso de que
        el número ingresado sea negativo.
        El programa pedirá un número y desplegará la raíz cuadrado de dicho número.
        En caso de que ocurra un error definido, el programa desplegará el mensaje
        correspondiente."""

    ocurre_error = True

    try:
        if numero < 0:
            raise TypeError("No es posible calcular la raíz de un negativo.")
        print("La raíz cuadrada de %.2f es %.2f" % (numero, numero ** 0.5))
    except (TypeError) as mensaje:
        print("Ocurrió una excepción identificada.", mensaje)
    except ValueError as mensaje:
        print(mensaje)
    except:
        print("¡No sé qué pasó!")
    else:
        print("No hubo errorres.")
        ocurre_error = False
    finally:
        if ocurre_error:
            print("Lástima.")
        else:
            print("¡YAY!")

levanta_excepcion(25)
print("\n")

levanta_excepcion(-1)
print("\n")

levanta_excepcion(7j)

````
