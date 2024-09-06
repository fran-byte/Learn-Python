:page_with_curl: [README](../README_en.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 20. ERRORS

The stopping of a program is due to errors, we explain some types:

## Syntax

They report **SyntaxError** code, simply by reviewing the code we will be able to find the resolution:
````python
print("Python"
````
> File "main.py", line 2

                  ^
>SyntaxError: unexpected EOF while parsing
>
## Name
They occur when the system interprets that it must execute some function, method... 

but he does not find it defined. They return **NameError** code:



> <ipython-input-2-155163d628c2> in <module>()
> ----> 1 pint("Hello")

>NameError: name 'pint' is not defined

Normally these syntax and name errors are identified by any code editor before execution, 


## Semantic
They are very difficult to detect since they are operating errors.

````python
list1=[]
list1.pop() # We cannot pop any element from an empty list
````
>Traceback (most recent call last):
> File "main.py", line 2, in <module>
> list1.pop() # We cannot pop any element from an empty listIndexError: pop from empty list


If we want to avoid this error we would have to check if it is empty first:

````python
list1 = []

if len(list1) > 0:
    list1.pop()
````
