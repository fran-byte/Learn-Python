:page_with_curl: [README](../README.md) :pencil: [Exercises](/tests/indicetests.md)

# 4. TEXT FILES

In the following text string, we can identify each character using an index.
````python

word = "Python"
````

>"P" index 0 ... or ... - 6
>
>"y" index 1 ... or ... - 5
>
>"t" index 2 ... or ... - 4
>
>"h" index 3 ... or ... - 3
>
>"o" index 4 ... or ... - 2
>
>"n" index 5 ... or ... - 1

If we want to refer to any index we will do it in the following way between brackets [ ]:
````python
print (word[3])
````
> 'h'
````python
print (word[-5])
> 'y'
````

We can do _SLICING_ (Slicing), that is, take _**slices**_ from that previous text string:
````python
print (word[2:-1]) # A slice from index 2 to -1 but without taking the latter
````
> 'tho'

````python
print (word[:2]) # From the start (since we have left it empty)
# to position 2, but without taking the latter, that is, index 0 and 1
````
> 'Py'
>
If we do not specify between the brackets, no number will be collected from the beginning to the end [:]

On the contrary, if we indicate an index that does not exist, we will get an error.
