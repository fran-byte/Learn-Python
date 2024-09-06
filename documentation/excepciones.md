:page_with_curl: [README](../README.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 22. EXCEPCIONES try / except

Para poder continuar con la ejecución del programa existen estos bloques de código, las excepciones.

````python
try:
    n = float(input("Introduce un número: "))
    m = 4
    print("{}/{} = {}".format(n,m,n/m))
except:
    print("Ha ocurrido un error, introduce bien el número")
````
Si se genera algún error ejecutará el bloque "except", es un bloque alternativo, que incluso podríamos dar otra oportunidad para salvar el error, 
si volvieramos a ejecutar el código previo, avisando previamente del fallo, para no cometerlo de nuevo.

## Bloque else añadido después de una excepción

````python
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien
````

## Bloque finally

Se ejecutará siempre, tengamos o no un error.

````python
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien
    finally:
        print("Fin de la iteración") # Siempre se ejecuta
````

