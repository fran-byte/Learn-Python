:page_with_curl: [README](../README.md) :pencil: [Exercises](/tests/indicetests.md)

# 9. for
## Looping through LISTS

In Python **for** is often used to loop through the contents of lists, tuples, dictionaries, etc...
We could do it with **while** but the lines of code would be longer

````python
ns = [1,2,3,4,"FIVE",6,7,"EIGHT",9]
for number in ns: # We are going to pass the contents of each index of (ns) to (number) and it will not end until it has looped through the entire index
# this index of (ns) will automatically increase.
print(number)
````

>1
>2
>3
>4
>FIVE
>6
>7
>EIGHT
>9

## Looping through LISTS and MODIFYING THEM
## in enumerate()

````python
ns = [1,2,3,4,5,6,7,8,9]
for index,number in enumerate(ns): # The contents of (ns) to (number) and the numeric index to (index) (LOOPING THROUGH THE LIST)
ns[index]*=10 # Multiplication in assignment (MODIFYING THE LIST)
print(ns[index])
````
Note that **enumerate**(ns) returns 2 values, one is the record number or index and the other is the content of that index,
the index will remain in the variable (index) that we have created in the (for) itself and the content of that index will go to (number)

It may seem a bit confusing at first but as we do exercises it will be very easy...

## ITERATING (going through) with zip

If we want to go through or iterate two lists at the same time, we can do it using the zip function and using a counter

````python
list1 = [1,"TWO",3,"FOUR",5,"SIX",7,"EIGHT",9]
list2 = ["ONE",2,"THREE",4,"FIVE",6,"SEVEN",8,"NINE"]
counter=0
for i,a in zip(list1,list2): # Each list will be dumped into (i) and (a) respectively

print(list1[counter],list2[counter])
counter+=1 # We are increasing the (counter) that will be our index to go looping through lists and printing
````

>1 ONE

>TWO 2

>3 THREE

>FOUR 4

>5 FIVE

>SIX 6

>7 SEVEN

>EIGHT 8

>9 NINE

The only drawback is that both lists must have the same number of elements
