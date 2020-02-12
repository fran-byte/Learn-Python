:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 20. EXCEPCIONES try / except

Para poder continuar con la ejecución del programa existen estos bloques de código, las excepciones.

````python
try:
    n = float(input("Introduce un número: "))
    m = 4
    print("{}/{} = {}".format(n,m,n/m))
except:
    print("Ha ocurrido un error, introduce bien el número")
````
Si se genera algún error ejecutara el bloque "except", es un bloque alternativo, que incluso podriamos dar otra oportunidad para salvar el error, 
si volvieramos a ejecutar el código previo, avisando previamente del fallo, para no cometerlo de nuevo.