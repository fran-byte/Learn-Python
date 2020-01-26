:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 12. CONJUNTOS { } 
## Colección DESORDENADA de elementos ÚNICOS

No pueden contener ningún elemento duplicado.

Su utilidad está asociada a pruebas de pertenencias a grupos y eliminación de elementos duplicados.

````python
conjunto1 = set() # Definiendo un conjunto vacío
conjunto1 = {1,2,3}

conjunto1.add(0)
conjunto1.add(3) # Aunque añadamos 3, como ya lo contiene, no lo añadirá

print(conjunto1)
````

>{0, 1, 2, 3}

ELIMINANDO elementos DUPLICADOS de otras Colecciones

````python
lista1 = [1,2,3,4,4,3,2,1] # Esta lista contiene elementos repetidos
c = set(lista1) # creamos un conjunto (c) que tiene por elementos la lista1

lista1 = list (c) # volvemos a generar la (lista1) con el contenido de (c)

print (lista1) # Y como vemos el paso de los elementos por el conjunto (c) ha eliminado los duplicados
````
>[1, 2, 3, 4]

>