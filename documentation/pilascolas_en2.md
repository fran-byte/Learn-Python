:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

# 14. PILAS(LIFO) and COLAS(FIFO)
## PILAS = Last In First Out, .append() .pop()

There are no PILAS in Python, so the best solution to create this abstract PILA would be to create an object using a class,
but we will see that later.
now we will simulate it this way:

````python
pila = [3,4,5]
pila.append(6) # Remember that append() adds an appendix to the end of the list
pila.append(7)
print(pila)

a = pila.pop() # .pop() extracts the last data from the list and if it is not stored it is lost.
print(a) # This is the last data entered and the first to leave (LIFO)
print(stack)
````
>[3, 4, 5, 6, 7]
7
[3, 4, 5, 6]

## QUEUES = First In First Out, from collections import deque
## .append() .popleft()

They are container objects of the deque type, they can perform operations in both directions, adding or removing elements.
To create a queue in Python we need to import the «deque» class from the «collections» package.

````python
from _collections import deque # First we import the deque class from the collections package
cola = deque() # empty
cola = deque(['Paco','Luis','Alvaro'])
print(cola)

cola.append('Oscar') # we add an element to the queue
print(cola)

cola.popleft() # It will take out the first one in the list....
# and since we haven't stored it, that element will be lost...
print(cola)

````
>deque(['Paco', 'Luis', 'Alvaro'])
deque(['Paco', 'Luis', 'Alvaro', 'Oscar'])
deque(['Luis', 'Alvaro', 'Oscar'])
