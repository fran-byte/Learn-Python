:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

# 11. TUPLES ()
## IMMUTABLE Data Collection

They accept all parameters just like lists, except those that imply modification.

```python
tuple1 = (100,"hello",[1,2,3,4])
print(tuple1.count(100)) # (count) will return the number of times the number 100 appears
# within this tuple.
```

> If we try to modify a Tuple (which is IMMUTABLE):

```python tuple1 = (100,"hello",100,[1,2,3,4]) tuple1[0]=50 ``` 

>Traceback (most recent call last): File "main.py", line 2, in <module> tuple1[0]=50 TypeError: 'tuple' object **does not support item assignment**
