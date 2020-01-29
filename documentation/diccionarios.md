:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 12. DICCIONARIOS {Clave:Valor} 
## Colecciones DESORDENADAS

Es una estructura de datos que pueden contener cualquier tipo de ellos: enteros, cadenas, listas e incluso otras funciones.
Podemos identificar cada elemento mediante una clave (Key).
````python
color = {'amarillo':'yellow','azul':'blue','verde':'green'}
print (color['azul'])
print (color)
````
>blue  
{'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}

### Modificando, Borrando, Operando o Mostrando valores de un diccionario.

````python
color['amarillo']='YELLOW'  # Le decimos que esta (clave) tendrá un nuevo (valor)
print (color['amarillo'])

del(color['amarillo']) # Con la función (del) podemos borrar cualquier clave/valor
print (color)
````
>YELLOW  
{'azul': 'blue', 'verde': 'green'}

````python
altura={'Paco':196,'Luis':177,'Alvaro':159}
print('La suma de la altura de Paco y Alvaro son ',altura["Paco"]+altura['Alvaro'],"Cm")
````
>La suma de la altura de Paco y Alvaro son  355 Cm

### RECORRIENDO los ELEMENTOS del DICCIONARIO

Mostrando tanto las claves como sus valores.

````python
altura={'Paco':196,'Luis':177,'Alvaro':159}
for clave in altura:
    print(clave,altura[clave])
````
>Paco 196  
Luis 177  
Alvaro 159  

#### Aunque la forma CORRECTA de recorrelo es con items()