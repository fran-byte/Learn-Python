:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 15. Entradas desde el terminal SCRIPTS 
## import sys / sys.argv

No todo va a ser escribir código en el intérprete, 
los programas informáticos fucionan de otra forma. Se crean ficheros con las instrucciones y a estos se les llaman scripts (o guiones de instrucciones). 
Eviamos ese fichero al intérprete desde la terminal (ya que python es un lenguaje interpretado), y se ejecutará.  

Y también estos Scripts pueden recibir datos desde el terminal en el momento de la ejecución.

Veamos un ejemplo:

````python
import sys
if len(sys.argv)==3:
    texto = sys.argv[1] # introducimos en la variable texto el argumento 1 tecleado por terminal
    repeticiones = int (sys.argv[2])    # introducimos en la variable repeticiones el argumento 2 tecleado por terminal
                                        # y lo convertimos a entero.
    for i in range(repeticiones):
        print(texto)

else:
    print("Error en los argumentos")
    print("nombre.py 'texto' nºrepeticiones")
````

````shell script
C:\Users\franc\Desktop>script1.py hola 6
hola
hola
hola
hola
hola
hola

````
Véase en esta ejecución por terminal:

>script1.py hola 6

Tiene 3 argumentos  

Argumento[0] que es el nombre del archivo: script1.py  

Argumento[1] 'hola'  

Argumento[2] 6  