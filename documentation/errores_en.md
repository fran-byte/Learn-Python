:page_with_curl: [README](../README_en.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 20. ERRORES

La detención de un programa se debe a errores, explicamos algunos tipos:

## Sintaxis

Nos reportan código **SyntaxError**, simplemente repasando el código poderemos dar con la resolución:
````python
print("Python"
````
>  File "main.py", line 2

                  ^
>SyntaxError: unexpected EOF while parsing
>
## Nombre
Se producen cuando el sistema interpreta que debe ejecutar alguna función, método... 

pero no lo encuentra definido. Devuelven el código **NameError**:



> <ipython-input-2-155163d628c2> in <module>()
> ----> 1 pint("Hola")

>NameError: name 'pint' is not defined

Normalmente estos errores sintácticos y de nombre son identificados por cualquier editor de código antes de la ejecución, 


## Semántico
Son muy difíciles de detectar ya que son errores de funcionamiento.

````python
lista1=[]
lista1.pop() # No podemos sacar ningún elemento de una lista vacía
````
>Traceback (most recent call last):
>  File "main.py", line 2, in <module>
>    lista1.pop() # No podemos sacar ningún elemento de una lista vacíaIndexError: pop from empty list


si queremos evitar este error habría que comprobar si está vacía primero:

````python
lista1 = []

if len(lista1) > 0:
    lista1.pop()
````
