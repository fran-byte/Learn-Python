:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

# 20. BUILT-IN FEATURES

Some of the functions:

## int()
Transform a string to an integer (if it is not possible it gives an error):

````python
n = int("10")
print(n)
````
>10

## float()
Transform a string to a float (if not possible it gives an error):

````python
f = float("10.5")
print(f)
````
>10.5
## str()
Transform any value to a string:

````python
c = "One text and two numbers " + str(10) + " y " + str(3.14)
print(c)
````
>One text and two numbers 10 and 3.14
>
## bin()
Integer to binary conversion:

````python
print(bin(10))
````
>0b1010
## hex()
Conversion from integer to hexadecimal:





## hex(10)
int(number, base)
Reconversion to integer (base 10):
````python
print(int('0b1010', 2))
print(int('0xa', 16))
````

## abs()
Absolute value of a number (distance):

````python
print(abs(-10))
````
>10
## round()
Rounding of a float to an integer, less than .5 downwards, greater than or equal to .5 upwards:

````python
print(round(5.5))
print(round(5.4))
````
>6
>5
## eval()
Evaluates a string as an expression, accepting variables if they have been previously defined:
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
Length of a collection or chain:

````python
print(len("A string"))
print(len([]))
````
>10
>0
## help()
Invoke the Python interpreter help menu:

````python
help()
````
>Welcome to Python 3.7's help utility!

>If this is your first time using Python, you should definitely check out
>the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

>Enter the name of any module, keyword, or topic to get help onwriting
>Python programs and using Python modules.  To remove this help utility and
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
