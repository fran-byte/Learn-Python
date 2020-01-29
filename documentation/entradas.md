:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 15. Entradas desde el terminal SCRIPTS 
## import sys / sys.argv

No todo va a ser escribir código en el intérprete, 
los programas informáticos fucionan de otra forma. Se crean ficheros con las instrucciones y a estos se les llaman scripts (o guiones de instrucciones). 
Eviamos ese fichero al intérprete (ya que paython es un lenguaje interpretado)desde la terminal, y se ejecutará.  

A También estos Scripts pueden recibir datos desde el terminal en el momento de la ejecución.

Veamos un ejemplo:

````python
import sys
if len(sys.argv)==3:
    texto = sys.argv[1]
    repeticiones = int (sys.argv[2])
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

C:\Users\franc\Desktop>
````