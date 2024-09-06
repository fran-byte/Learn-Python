:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

# 10. for We continue iterating
## "Modifying on the fly" (immutable) strings

They cannot really be modified, but we are going to do something similar.

Create a new string (str) that will start from a modification of the first one.

````python
string1 = "Python"
string2 = ""

for character in string1:
string2+=character*2 # A simple modification multiplying the element x 2
print(string2)

````
> PPyytthhoonn

## Simulating (for) as if it were other languages

````python
for i in range(10): # 0 to 9
print(i)
````

>0
>1
>2
>3
>4
>5
>6
>7
>8
>9

**range** (x,y,z)

x = will be the start from where the (for) will start to iterate (if not set, by default it will be 0)

y = the value that represents that range (-1)

z = will be the increment, if left empty, by default it will be 1
