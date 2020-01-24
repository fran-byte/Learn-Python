:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)


# 7. CONTROL DE FLUJO if, elif, else

Condicionales

````python
if a==5: # El (if) siempre viene precedido de los 2 puntos (:) no olvidarlo, si no, nos reportará un error.
    print("Correcto a = 5") # Observese que el (print) dentro del (if) esta sangrado o identado.

else:
     print("a es distito de 5") # Si la condición no fueta verdadera (True) imprimiriamos esto
````

Podemos añadir después de un (if) un (elif) y seguir introduciendo condiciones.

````python
if a==5: 
    print(a) 

elif a==15:
    print(a) 
else:
     print("a no es ni 5 ni 10")
````
