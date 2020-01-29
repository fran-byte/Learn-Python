:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 16. SALIDAS (Formateo)
## .format

Con frecuencia necesitaremos más control sobre el formateo de tu salida, o simplemente imprimir valores separados por
espacios.
El tipo string contiene algunos métodos útiles para emparejar cadenas, alinear y sacar de una manera elegantecon un determinado ancho; 
con str.format().

````python
v = 'otro texto'
n = 10
print('un texto {} y un número {}'.format(v,n)) # Hemos dejado las variables v y n en los corchetes
````

>un texto otro texto y un número 10

Por defecto las posiciones de las llaves y variables coinciden respectivamente, si las queremos alterar:

````python
v = 'otro texto'
n = 10
print('un texto {1} y un número {0}'.format(v,n)) # Hemos dejado las variables v y n en los corchetes
````
>un texto 10 y un número otro texto

También podemos colocar dentro de los corchetes variables.

````python
print("{:>30}".format("palabra"))  # Esta palabra saldrá formateada con 30 espacios a la derecha

print("{:^30}".format("palabra"))  # Esta palabra saldrá formateada con 15 espacios a derecha y 15 a izquierda

print("{:.5}".format("palabra"))  # Esta palabra saldrá TRUNCADA, es decir que solamente saldrán los 5 primeros caracteres
````
>                       palabra  
           palabra  
palab  

````python
print('{:>30.3}'.format('palabra'))  # TRUNCAMIENTO y MARGEN
````
>                           pal