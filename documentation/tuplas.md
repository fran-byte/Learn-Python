:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 11. TUPLAS () 
## Colección de Datos INMUTABLE

Aceptan todo los parámetros al igual que las listas, menos los que impliquen modificación.

````python
tupla1 = (100,"hola",[1,2,3,4])
print(tupla1.count(100))   # (count) nos devolverá el número de veces que aparece el número 100
                    # dentro de esta tupla.
````
>1

Si intentamos modificar una Tupla (que es INMUTABLE):

````python
tupla1 = (100,"hola",100,[1,2,3,4])
tupla1[0]=50
````
>Traceback (most recent call last):  
  File "main.py", line 2, in <module>  
    tupla1[0]=50  
TypeError: 'tuple' object **does not support item assignment**