
:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)




#2- VARIABLES and DATA TYPES

## Defining a variable

In Python, variables are created when they are defined for the first time.
You can store text, numbers or more complex structures.
It is recommended that the name of the variable be related to what is going to be stored in it.
They cannot start with any number.
````python
greeting1= "Good morning" # (this is a comment in Python, we will use the symbol: # and then the text)
````

## Reserved words in Python

They cannot be used to name variables:

|  |  | |  | | |
| :--- | :--- | :--- | :--- | :--- | :--- |
| and | as | assert | async | await | break |
| continue | def | del | elif | else | except |
| false | finally | for | from | global | if |
| import | in | is | lambda | none | nonlocal |
| not | or | pass | raise | return | true |
| try | while | with | yield |


### We will start with the types that exist, 
(Although we will delve into each of them later)
## Guy. Strings (str) or Strings ""
They are text enclosed in quotes (single or double) and accept operators.

They are immutable
````python
string1 = "double quotes"
string2 = 'single quotes'

a = "Good"
b = "days!"
sumStrings = a + " " + b
print (sumStrings)
````
## Type. Booleans
It can only admit True or False. Used in conditions and loops, which we will see later.
True/False
````python
a = 5
print(a==5) # We are telling it to print the condition of that equality on the screen and it will return:
true
````



## Type. Numbers
### Integers:

They are the Numbers that lack decimals
**int** (integer) or **long** (long integer for more precision).
`````python
age = 25
`````
### Real: 

They are numbers that have decimals and are of type float.
`````python
length = 25,638
`````
### Complexes:

Numbers that have a real part and an imaginary part. These numbers are called complex.
`````python
n = 3.8 + 9j
`````

 

## Type. Sets {}
Collection of data without repeated elements, unordered and separated by commas, enclosed in braces.
`````python
set = {'house', 'tree', 'dog',356,'dumpling',-89,'mango', 'cheese'}
`````

## Type. Lists [ ]
They are ordered sets of elements that can store numbers, strings, other lists...
They are placed between ([ ]) and the elements are separated by commas.

`````python
list1 = ['17',-66,99,44,"bye", 'hello',6,7,"8",9,10,11,12,13]
list2 = list1[0:8:2] # We take from list1 from position 0 to 8 and from 2 2n 2; and we put it in the list2
print(list2)
['17', 99, 'goodbye', 6] 
`````
 

## Type. Tuples ()
It is an **immutable** list
`````python
tuple1 = ("bird",34,"9",clock)
`````

## Type. Dictionaries { : }
We can store any type of value such as integers, strings, lists and even other functions.
And we can identify each element by a key (Key).
`````python
dictionary1 = {'car': 'Mercedes', 'Color': 'red', 'speed': 280 }
print (dictionary1['car']) # By entering the key "car" we will get "Mercedes"
`````
