:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 20. ERRORES

La detención de un programa se debe a errores, explicamos algunos tipos:

## Sintaxis

Nos reportan código **SyntaxError**, simplemente repasando el código poderemos dar con la resolución:
````python
print("Python"
````
>  File "main.py", line 2

>                  ^
>SyntaxError: unexpected EOF while parsing
>
## NOMBRE
Se producen cuando el sistema interpreta que debe ejecutar alguna función, método... 

pero no lo encuentra definido. Devuelven el código **NameError**:



> <ipython-input-2-155163d628c2> in <module>()
> ----> 1 pint("Hola")

>NameError: name 'pint' is not defined

Normalmente estos errores sintácticos y de nombre son identificados por cualquier editor de código antes de la ejecución, 


## SEMÁNTICO
Son muy difíciles de detectar ya que son errores de funcionamiento.

````python
lista1=[]
lista1.pop() # No podemos sacar ningún elemento de una lista vacía
````
>Traceback (most recent call last):
>  File "main.py", line 2, in <module>
>    lista1.pop() # No podemos sacar ningún elemento de una lista vacíaIndexError: pop from empty list

Si intentamos sacar un elemento de una lista vacía, algo que no tiene mucho sentido, el programa dará fallo de tipo IndexError. Esta situación ocurre sólo durante la ejecución del programa, por lo que los editores no lo detectarán:

Código
Resultado

<ipython-input-6-9e6f3717293a> in <module>()
----> 1 l.pop()

IndexError: pop from empty list
Para prevenir el error deberíamos comprobar que una lista tenga como mínimo un elemento antes de intentar sacarlo, algo factible utilizando la función len():


l = []

if len(l) > 0:
    l.pop()
Ejemplo lectura de cadena y operación sin conversión a número

Cuando leemos un valor con la función input(), éste siempre se obtendrá como una cadena de caracteres. Si intentamos operarlo directamente con otros números tendremos un fallo TypeError que tampoco detectan los editores de código:

Código
Resultado

Introduce un número: 4

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-12-85bb893ab3e3> in <module>()
----> 1 print("{}/{} = {}".format(n,m,n/m))

TypeError: unsupported operand type(s) for /: 'str' and 'int'
Como ya sabemos este error se puede prevenir transformando la cadena a entero o flotante:

Código
Resultado

Introduce un número: 10
10.0/4 = 2.5
Sin embargo no siempre se puede prevenir, como cuando se introduce una cadena que no es un número:

Código
Resultado

Introduce un número: aaa

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-14-c0e7fd4a26a9> in <module>()
----> 1 n = float(input("Introduce un número: "))
    2 m = 4
    3 print("{}/{} = {}".format(n,m,n/m))

ValueError: could not convert string to float: 'aaa'
Como podéis suponer, es difícil prevenir fallos que ni siquiera nos habíamos planteado que podían existir. Por suerte para esas situaciones existen las excepciones.