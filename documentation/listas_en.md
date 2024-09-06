:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

# 5. LISTS [ ]

They can be text strings, characters, other lists, they go between brackets [ ] and are MODIFIABLE

````python
list1 = ["Python",1,2,"3",[4,5,"six"],7,8] # We can see another list between brackets inside list1
print (list1)
````

>['Python', 1, 2, '3', [4, 5, 'six'], 7, 8]
>
We can do **_Slicing_** with lists too:
````python
print (list1[2:6])
````
>[2, '3', [4, 5, 'six'], 7]
>
Modify them.
````python
list1[3]="THREE"
print (list1)
````
>['Python', 1, 2, 'THREE', [4, 5, 'six'], 7, 8]

Using the **_len_** function we can know the length of that list.
````python
print (len(list1))

````
>7
>
>
We will use the following functions as we progress...

## Methods (or functions) to work with LISTS in Python

list = **list()** # Declaration of a list

**len**(list) # Counts the number of elements in the list

list.**insert**(pos, x) # Adds an element (x) to the end of the list.

list.**extend**(list2) # Joins two lists (joins list2 (the one passed as parameter) to the list)

list.**remove**(x) # Deletes the first element from the list whose value is x. If it does not exist, an error is returned

list.**pop**(pos) # Deletes the element at the given position from the list, and returns it.

**del** list[:] # Deletes all elements from the list (list.clear())

list.**index**(x) # Returns the index in the list of the first element whose value is x.

list.**count**(x) # Returns the number of times x appears in the list.

list.**sort**(cmp=None, key=None, reverse=False) # Sorts the items in the list

list.**reverse**() # Reverses the elements in the list.

listCopy = list[:] # Returns a copy of the list (list.copy())
