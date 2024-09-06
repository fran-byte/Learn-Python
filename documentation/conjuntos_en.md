:page_with_curl: [README](../README_en.md)  :pencil: [Exercises](/tests/indicetests.md)

# 12. SETS { }
## UNORDERED collection of UNIQUE elements

They cannot contain any duplicate elements.

Their usefulness is associated with group membership tests and elimination of duplicate elements.

````python
set1 = set() # Defining an empty set
set1 = {1,2,3}

set1.add(0)
set1.add(3) # Even if we add 3, since it already contains it, it will not be added

print(set1)
````

>{0, 1, 2, 3}

ELIMINATING DUPLICATE elements from other Collections

````python
list1 = [1,2,3,4,4,3,2,1] # This list contains repeated elements
c = set(list1) # we create a set (c) that has list1 as elements

list1 = list (c) # we regenerate (list1) with the content of (c)

print (list1) # And as we see the passage of elements through the set (c) has eliminated the duplicates
````
>[1, 2, 3, 4]

>
