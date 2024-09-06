
:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)




# 3- INPUTS and OUTPUTS

## print()

This function allows us to _**display**_ text on the screen,
the function argument will be in parentheses, and can be a text between single or double quotes or a variable.

````python
print ("Hello World")
x = 5
print (x)

````
> Hello World
>
> 5
````python
print (""" With these 3 quotes and with
an ENTER per line we can change lines as many times as we want and thus
we do not have to put several prints.""")
````
> With these 3 quotes and with
> an ENTER per line we can change lines as many times as we want and thus
we do not have to put several prints.

If we want to include quotes within quotes, we do it with a backslash ( \\ )
````python

print ("This backslash will not come out but it leaves the following character raw \" which are these quotes \"")
````
> This backslash will not come out but it leaves the following character raw " which are these quotes "
---
````python
print ("We can use \nTo make a line break, or a \tfor a tab")
````
> We can use
>
> To make a line break, or a ____for a tab

## input()

This function allows us to collect **_text_** on the screen,
the function argument will be in parentheses, and it can be a text between single or double quotes.
We can collect it in a variable.

````python
text1 = input("Text input: ")
````
### Type Conversion:
We can also convert the input text to integers or floats and thus be able to operate with them.
````python
integerNumber = int (input ("Enter a number: "))
print(integerNumber+50)

decimalNumber = float (input ("Enter a decimal number: "))
print(decimalNumber+50)
````
