:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)


# 42. FICHEROS de TEXTO
## Creación y Escritura

````python
from io import open

texto = "Una línea con texto\nOtra línea con texto"

# Ruta donde crearemos el fichero, w indica escritura (puntero al principio)
fichero = open('fichero.txt','w')  

# Escribimos el texto
fichero.write(texto) 

# Cerramos el fichero
fichero.close()
````

## Lectura
````python
from io import open

# Ruta donde leeremos el fichero, r indica lectura (por defecto ya es r)
fichero = open('fichero.txt','r')  

# Lectura completa
texto = fichero.read() 

# Cerramos el fichero
fichero.close()  

print(texto)
````

>Una línea con texto
>
>Otra línea con texto

