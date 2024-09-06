:page_with_curl: [README](../README.md) :books: [Educational material](/documentation/indicedocu.md) :pencil: [Exercises](/tests/indicetests.md) # 13. DICTIONARIES {Key: Value} ## UNORDERED Collections It is a data structure that can contain any type of data: integers, strings, lists and even other functions.
We can identify each element by a key (Key).
````python
color = {'yellow':'yellow','blue':'blue','green':'green'} print (color['blue']) print (color)
```
> blue {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}

### Modifying, Deleting, Operating on or Displaying values ​​​​from a dictionary.

```python
 color['yellow']='YELLOW' # We tell it that this (key) will have a new (value) print (color['yellow']) del(color['yellow'])
# With the (del) function we can delete any key/value print (color)
```

YELLOW {'azul': 'blue', 'verde': 'green'} ```python alta={'Paco ':196,'Luis':177,'Alvaro':159} print('The sum of the heights of Paco and Alvaro are ',high["Paco"]+high['Alvaro'],"Cm")  
```

>The sum of the heights of Paco and Alvaro are 355 Cm ### TRAVELING through the DICTIONARY ELEMENTS Showing both the keys and their values.

```python
 height={'Paco':196,'Luis':177,'Alvaro':159} for key in height: print(key,height[key])
```
>Paco 196 Luis 177 Alvaro 159 #### Although the CORRECT way to iterate through it is with _items()_
```python for c,v in heights.items(): # we are going to dump the key in 'c' and the value in 'v' print(c,v)
```

### ADVANCED COLLECTIONS DICTIONARY + LIST We are going to create several dictionaries and introduce them in a list.
```python
 characters=[] # Create an empty list p={'Name':'Gandalf','Class':'Wizard','Race':'Human'} # Create a dictionary characters.append(p )
# Add that dictionary to the list (p) p={'Name':'Legolas','Class':'Archer','Race':'Elf'}
# Create another character characters.append(p)
# Add it to the list # GO through the created list (p) for p in characters: print(p['Name'],p['Class'],p['Race']) ```` >Gandalf Wizard Human Legolas Archer Elf
