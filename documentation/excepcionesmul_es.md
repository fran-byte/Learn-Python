:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

#20. MULTIPLE EXCEPTIONS

If several different errors occur, it would be advisable for us to act differently in each case.

For this purpose, we are going to assign an exception to a variable and thus analyze the type of error thanks to its identifier
````python
try:
    n = input("Enter a number: ") # we do not transform to number
    5/n
except Exception as e: # save the exception as the variable e
    print("An error has occurred =>", type(e).__name__)
````

>
````python
try:
    n = float(input("Enter a divisor number: "))
    5/n
exceptTypeError:
    print("Cannot divide number by string")
except ValueError:
    print("You must enter a string that is a number")
except ZeroDivisionError:
    print("Cannot divide by zero, try another number")
except Exception as e:
    print("An unexpected error has occurred", type(e).__name__ )
````
