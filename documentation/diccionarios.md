:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 12. DICCIONARIOS {Clave:Valor} 
## Colecciones DESORDENADAS

Es una estructura de datos que pueden contener cualquier tipo de dato: enteros, cadenas, listas e incluso otras funciones.
Podemos identificar cada elemento mediante una clave (Key).
````python
color = {'amarillo':'yellow','azul':'blue','verde':'green'}
print (color['azul'])
print (color)
````
>blue  
{'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}

Modificando, Borrando, Operando o Mostrando valores de un diccionario.

````python
color['amarillo']='YELLOW'  # Le decimos que esta (clave) tendrá un nuevo (valor)
print (color['amarillo'])

del(color['amarillo'])
print (color)
````
>YELLOW  
{'azul': 'blue', 'verde': 'green'}