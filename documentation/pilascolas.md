:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 14. PILAS(LIFO) y COLAS(FIFO)
## PILAS = Last In First Out, .append() .pop()

En Python no existen las PILAS, asi que la solución para crear esa PILA abstracta la mejor solución sería crear un objeto mediante una clase,
 pero eso lo veremos más adelante.
ahora la simularemos de esta manera:

````python
pila = [3,4,5]
pila.append(6) # Recordemos que append() añade un apéndice al final de la lista
pila.append(7)
print(pila)

a = pila.pop() # .pop() extrae el último dato de la lista y si no se almacena se pierde.
print(a) # Este es le último dato introducido y el primero en salir (LIFO)
print(pila)
````
>[3, 4, 5, 6, 7]  
7
[3, 4, 5, 6]

## COLAS = First In First Out, from collections import deque
## .append() .popleft()

Son objetos contenedores de tipo deque, pueden realizar operaciones en ambas direcciones, añadir o eliminar elementos.
Para crear una cola en Python requerimos importar la clase «deque» desde el paquete «collections».

````python
from _collections import deque # Primero importamos la clase deque desde el paquete collections
cola = deque() # vacía
cola = deque(['Paco','Luis','Alvaro'])
print(cola)

cola.append('Oscar') # añadimos un elemento a la cola
print(cola)

cola.popleft()  # Nos sacará el primero que está en la lista.... 
                # y como no lo hemos almacenado ese elemento se perderá...
print(cola)

````
>deque(['Paco', 'Luis', 'Alvaro'])  
deque(['Paco', 'Luis', 'Alvaro', 'Oscar'])  
deque(['Luis', 'Alvaro', 'Oscar'])