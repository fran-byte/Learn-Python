:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 20. FUNCIONES INTEGRADAS

Algunas de las funciones:

## int()
Transforma una cadena a un entero (si no es posible da error):

````python
n = int("10")
print(n)
````
>10

## float()
Transforma una cadena a un flotante (si no es posible da error):

````python
f = float("10.5")
print(f)
````
>10.5
## str()
Transforma cualquier valor a una cadena:

````python
c = "Un texto y dos números " + str(10) + " y " + str(3.14)
print(c)
````
>Un texto y dos números 10 y 3.14
>
## bin()
Conversión de entero a binario:

````python
print (bin(10))
````
>0b1010
## hex()
Conversión de entero a hexadecimal:





## hex(10)
int(numero, base)
Reconversión a entero (base 10):
````python
print(int('0b1010', 2))
print(int('0xa', 16))
````

## abs()
Valor absoluto de un número (distancia):

````python
print(abs(-10))
````
>10
## round()
Redondeo de un flotante a entero, menor de .5 a la baja, mayor o igual a .5 al alza:

````python
print(round(5.5))
print(round(5.4))
````
>6
>5
##eval()
Evalúa una cadena como una expresión, acepta variables si se han definido anteriormente:
````python
print(eval('2 + 5'))
````
>7
````python
n = 10

print(eval('n * 10 - 5'))
````
>95

## len()
Longitud de una colección o cadena:

````python
print(len("Una cadena"))
print(len([]))
````
>10
>0
## help()
Invoca el menú de ayuda del intérprete de Python:

````python
help()
````
>Welcome to Python 3.7's help utility!

>If this is your first time using Python, you should definitelycheck out
>the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

>Enter the name of any module, keyword, or topic to get help onwriting
>Python programs and using Python modules.  To quit this help utility and
>return to the interpreter, just type "quit".

>To get a list of available modules, keywords, symbols, or topics, type
>"modules", "keywords", "symbols", or "topics".  Each module also comes
>with a one-line summary of what it does; to list the modules whose name
>or summary contain a given string such as "spam", type "modules spam".

>help>
>You are now leaving help and returning to the Python interpreter.
>If you want to ask for help on a particular object directly from the
>interpreter, you can type "help(object)".  Executing "help('string')"
>has the same effect as typing a particular string at the help>prompt.