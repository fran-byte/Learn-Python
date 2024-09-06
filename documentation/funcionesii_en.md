:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

#18. FUNCTIONS II
Sometimes we don't know the number of elements we are going to send to a function.

For these cases we will use the indeterminate parameters by position and by name.

## INDETERMINATE arguments per POSITION 

Receiving indeterminate parameters by position,

We send a dynamic list, a tuple really, and for that we define the parameter with an asterisk:

````python
def indet_pos(*args): ## (args) is not a reserved word, but is used by convention
    for arg in args:
        print(arg)

indet_pos("Phyton","Hello",3,[5,53,21,5])
````
>Phyton  
Hello  
3  
>[5, 53, 21, 5]
## INDETERMINATE arguments by NAME (or Key)
Receiving parameters by name (keyword args)

Obviously we have to create a dynamic dictionary with these arguments and to do this we define the parameter with two asterisks:

````python
def indet_word(**kwargs): ## (kwargs) is not a reserved word, but is used by convention.
    print(kwargs)

indet_word(m="Python", b="Hello", n=3, s=[1,2,3,4,5]) 
````
>{'m': 'Python', 'b': 'Hello', 'n': 3, 's': [1, 2, 3, 4, 5]}

## By Name and Position

Receiving from both types, for this we have to create 2 dynamic collections.

We send the indet arguments first. by value and then the key/value ones:

````python
def indet_mix(*args,**kwargs):
    multiplying = 1
    for arg in args:
        multiplying*= arg
    print("result = ", multiplying)
    for kwarg in kwargs:
        print(kwarg, "=", kwargs[kwarg])

indet_mix(3, 6, 8, name="Fran", age=22)
````
>result = 144  
name = Fran  
age = 22
>
