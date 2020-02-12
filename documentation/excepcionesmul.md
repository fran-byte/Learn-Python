:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 20. EXCEPCIONES MULTIPLES

Si ocurrieran varios errores diferentes, nos convendría actuar de forma diferente en cada caso.

Para este cometido, vamos a asignar una excepción a una variable y así analizar el tipo de error gracias a su identificador
````python
try:
    n = input("Introduce un número: ")  # no transformamos a número
    5/n
except Exception as e:  # guardamos la excepción como la variable e
    print("Ha ocurrido un error =>", type(e).__name__)
````

>
````python
try:
    n = float(input("Introduce un número divisor: "))
    5/n
except TypeError:
    print("No se puede dividir el número entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e:
    print("Ha ocurrido un error no previsto", type(e).__name__ )
````