:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

# 20. EXCEPTIONS try/except

In order to continue with the execution of the program, there are these blocks of code, the exceptions.

````python
try:
    n = float(input("Enter a number: "))
    m = 4
    print("{}/{} = {}".format(n,m,n/m))
except:
    print("An error has occurred, enter the number correctly")
````
If an error is generated, it will execute the "except" block, it is an alternative block, which we could even give another opportunity to save the error, 
if we were to re-execute the previous code, previously warning of the error, so as not to commit it again.

## else block added after an exception

````python
while(True):
    try:
        n = float(input("Enter a number: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("An error has occurred, enter the number correctly")
    else:
        print("Everything worked correctly")
        break # It is important to break the iteration if everything has gone well
````

## finally block

It will always be executed whether we have an error or not.

````python
while(True):
    try:
        n = float(input("Enter a number: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("An error has occurred, enter the number correctly")
    else:
        print("Everything worked correctly")
        break # It is important to break the iteration if everything has gone well
    finally:
        print("End of iteration") # Always executed
````
