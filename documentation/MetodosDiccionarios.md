:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 34. MÉTODOS - DICCIONARIOS
````python
colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }

````
## get()
Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto:

````python
colores.get('negro','no se encuentra')
Resultado

````
> 'no se encuentra'

## keys()
Genera una lista en clave de los registros del diccionario:

````python
colores.keys()
````
> dict_keys(['amarillo', 'azul', 'verde'])

## values()

Genera una lista en valor de los registros del diccionario:

````python
colores.values()

````
> dict_values(['yellow', 'blue', 'green'])


## items()
Genera una lista en clave-valor de los registros del diccionario:
````python
colores.items()
````
> dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')])
````python
for clave, valor in colores.items():
    print(clave, valor)
````
>amarillo yellow
>azul blue
>verde green

## pop()
Extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto:
````python
colores.pop("amarillo", "no se ha encontrado")
````
> 'no se ha encontrado'
````python
colores.pop("negro","no se ha encontrado")
````
> 'no se ha encontrado'

## clear()
Borra todos los registros de un diccionario:
````python
colores.clear()
colores
````
> {}