:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

# 7. FLOW CONTROL if, elif, else

Conditionals

````python
if a == 5: # The (if) is always preceded by 2 dots (:) do not forget it, otherwise it will report an error.
print("Correct a = 5") # Note that the (print) inside the (if) is indented.

else:
print("a is different from 5") # If the condition is not true we would print this
````

We can add an (elif) after an (if) and continue introducing conditions even nested (in if or else)
````python
if a >= 5:
print(a)

elif a == 15:
print(a)
else:
print("a is neither 5 nor 15")
if a == 10: # We have this (if) nested inside the (else).
print(a)
````
