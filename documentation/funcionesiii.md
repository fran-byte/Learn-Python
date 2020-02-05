:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 19. FUNCIONES III
## Funciones RECURSIVAS (SIN RETORNO)
Se utilizan para subdividir en tareas más simples el código.
Son funciones que se llaman a sí mismo. Tienen un cierto parecido a un bucle o iteración.

````python
def contador(number):
    number *= 2
    if number <100:
        print(number)
        contador(number)
    else:
        print("number superó los 100 se nos fue a ", number)
        
    

contador(2)
````
## Funciones RECURSIVAS (CON RETORNO)

Podemos realizar un ejercicio para mostrar el factorial de un número.

````python
def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num -1)
    print("valor final ->",num)
    return num

print(factorial(5))

````

>Valor inicial -> 5  
Valor inicial -> 4  
Valor inicial -> 3  
Valor inicial -> 2  
Valor inicial -> 1  
valor final -> 1valor final -> 2  
valor final -> 6  
valor final -> 24  
valor final -> 120  
120