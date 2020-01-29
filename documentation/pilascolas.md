:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 14. PILAS(LIFO) y COLAS(FIFO)
## PILAS = Last In First Out / .append() .pop()

En Python no existen las PILAS, asi que la solución para crear esa PILA abstracta la mejor soluciión seria crear un objeto mediante una clase,
 pero eso lo veremos más adelante.
ahora la simularemos de esta manera:

````python
pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)

a = pila.pop()
print(a) # Este es le último dato introducido y el primero en salir (LIFO)
print(pila)
````
>[3, 4, 5, 6, 7]  
7
[3, 4, 5, 6]
