:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

#17. FUNCTIONS
## def name()

They are blocks of code to which a name is associated, may or may not receive arguments as input, follows a sequence of statements performing a task and can be called as many times as necessary.

Instead of repeating blocks and blocks of the same or similar code, we created functions that would take care of those redundant tasks.


````python
def test(): # This function will not receive any arguments.
    return "text",20,[1,2,3]

print(test())
````
>('text', 20, [1, 2, 3])

The values ​​that are received are called parameters, 
and during the call the values ​​that are sent are called arguments.

## Sent Arguments by POSITION (order)
When we send arguments to a function, they are received in order, (called positional arguments)


````python
def subtraction(a,b): # This function will receive 2 arguments (1,2) and they will go in ORDER 1 will be 'a' and 2 will be 'b'
    return a-b

print(subtraction(1,2))
````
>-1

## Sent Arguments by NAME
It is possible to change this order of the parameters if 
We indicate during the call what value each parameter has from its name.
````python
def subtraction(a,b): # This function will receive 2 arguments (1,2) and they will go by NAME 1 will be 'a' and 2 will be 'b'
    return a-b

print(subtraction(b=2,a=1))
````
>-1

## Sending ERRORS in returns

````python
def subta(a=None, b=None): # We declare these variables directly with None (empty)
    if a==None or b==None:
        print("Error, send 2 numbers to the function")
    else:
        return a-b
print(subtraction(1,2))
````
## Passing Arguments by VALUE
These numbers are passed by VALUE and a copy is created inside the function, 
That is why what we do with them does not affect them externally:
````python
def double_value(number):
    number *= 2 
    return number
n = 10 # if we place this variable here it will mean that what we do in the function will have no effect
double_value(n)
print(n) 
````
>10

## If what we want is for passing by VALUE in a variable to "work" for us
We are going to return the result and not the variable.

````python
def double_value(number):
    return number*2 # We pass the result and not the variable

n = 10 
n=double_value(n)
print(n) 
````
>20

## Passing Arguments by REFERENCE

On the other hand, lists or other collections, since they are composite types, are passed by REFERENCE, 
and here if we modify them inside the function now they will also remain modified outside:

````python
def double_values(numbers):
    for i,n in enumerate(numbers):
        numbers[i]*=2 
ns=[10,50,100]
double_values(ns)
print (ns)

````
>[20, 100, 200]



## We can also CREATE a COPY of the call to Avoid Modifications
````python
def double_values(numbers):
    for i,n in enumerate(numbers):
        numbers[i]*=2 
ns=[10,50,100]
double_values(ns)
print (ns[:]) # we are not sending 'ns' but a COPY of 'ns'
````
