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
print('{:>30.3}'.format('palabra'))  # TRUNCAMIENTO de 3 caracteres y MARGEN de 30 espacios
````
>                           pal


- Vamos a formatear números enteros y rellenarlos con espacios a la izquierda:

````python
print('{:4d}'.format(10)) # Rellenado con espacios (4) número entero(d)
print('{:4d}'.format(100))
print('{:4d}'.format(1000))
````

>  10  
 100  
1000  

````python
print('{:04d}'.format(10)) # Rellenado con CEROS (4) número entero(d)
print('{:04d}'.format(100))
print('{:04d}'.format(1000))
````
>0010  
0100  
1000  

- Ahora formateamos decimales:

````python
print('{:07.3f}'.format(42.12345)) 
````
>042.123

El número total de caracteres de este margen será el 7, incluido el punto, y el rellenado será ceros que colocamos delante del número 7
Lo que tenemos después del punto serán los flotantes (Decimales) que serán 3