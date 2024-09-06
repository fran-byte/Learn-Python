:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

#16. OUTPUTS (Formatting)
## .format

Often you'll need more control over formatting your output, or simply printing values ​​separated by
spaces.
The string type contains some useful methods for elegantly matching strings, aligning, and popping them to a given width; 
with str.format().

````python
v = 'other text'
n = 10
print('a text {} and a number {}'.format(v,n)) # We have left the variables v and n in the square brackets
````

>a text another text and a number 10

By default the positions of the keys and variables coincide respectively, if we want to alter them:

````python
v = 'other text'
n = 10
print('a text {1} and a number {0}'.format(v,n)) # We have left the variables v and n in the square brackets
````
>a text 10 and a number another text

We can also place variables inside the brackets.

````python
print("{:>30}".format("word")) # This word will be formatted with 30 spaces to the right

print("{:^30}".format("word")) # This word will be formatted with 15 spaces on the right and 15 on the left

print("{:.5}".format("word")) # This word will be TRUNCATED, that is, only the first 5 characters will be output
````
> word  
           word  
word  

````python
print('{:>30.3}'.format('word')) # TRUNCATION of 3 characters and MARGIN of 30 spaces
````
> pal


- Let's format whole numbers and fill them with spaces on the left:

````python
print('{:4d}'.format(10)) # Padding with spaces (4) integer(d)
print('{:4d}'.format(100))
print('{:4d}'.format(1000))
````

> 10  
 100  
1000  

````python
print('{:04d}'.format(10)) # Padded with ZEROS (4) integer(d)
print('{:04d}'.format(100))
print('{:04d}'.format(1000))
````
>0010  
0100  
1000  

- Now we format decimals:

````python
print('{:07.3f}'.format(42.12345)) 
````
>042.123

The total number of characters in this margin will be 7, including the period, and the padding will be zeros that we place in front of the number 7
What we have after the point will be the floats (Decimals) which will be 3
