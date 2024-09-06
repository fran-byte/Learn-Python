:page_with_curl: [README](../README.md) :pencil: [Exercises](/tests/indicetests.md)

# 6. NESTED LISTS[ ]

As we said before we can include lists inside another list

````python
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

r = [a,b,c]

print (r)
````
> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

If we want to access any of these numbers we must first access the _**first index**_
that will correspond to one of the 3 lists, and then a _**second index**_ that will correspond to one of the numbers
in the list, we will see this with an example.

````python
print(r[2][1]) # First index[2] corresponds to the 3rd group, that is, to the list "c" already nested within "r"
# and the second index [1] to the number 8 (we always start counting from index 0)
````
> 8

### Modifying NESTED LISTS
In the previous example, we are going to add the first 2 indices of the lists (nested) that we have introduced and leave it at the third index.

````python
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

r = [a,b,c] # This is what we have now inside r = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

r[0][2] = sum (r[0][:2]) # We are adding r[0][:2] from index [0] (i.e. the old list "a" now nested in "r")
# from [:2] index 0 since we have not put any start until index 2 (remember that the latter is not taken)
# and we leave this sum in r[0][2] the list "a" already nested in r [0] and inside this in index [2]

r[1][2] = sum (r[1][:2]) # We do the same with the rest of the indexes
r[2][2] = sum (r[2][:2])

print ("The result is the following: ",r)
````
> The result is the following: [[1, 2, 3], [4, 5, 9], [7, 8, 15]]
