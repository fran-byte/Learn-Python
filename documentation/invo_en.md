:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

# 24. INVOKING EXCEPTIONS

We can call an error manually.
````python
def error_function(something=None):
    if something is None:
        print("Error! A null value is not allowed (with a print)")

error_function()
````

## raise

Sometimes it is possible to identify a situation in which a certain condition will cause an error. In that case an exception can be raised before the error occurs and a corresponding message issued.

The raise expression is used to raise exceptions defined by the programmer.

````python
def raise_exception(number):
    """ Will raise an exception with its own message in case
        the number entered is negative.
        The program will ask for a number and display the square root of that number.
        In case a defined error occurs, the program will display the message
        corresponding."""

    error_occurs = True

    try:
        if number < 0:
            raise TypeError("The root of a negative cannot be calculated.")
        print("The square root of %.2f is %.2f" % (number, number ** 0.5))
    except (TypeError) as message:
        print("An identified exception occurred.", message)
    except ValueError as message:
        print(message)
    except:
        print("I don't know what happened!")
    else:
        print("There were no errors.")
        error_occurs = False
    finally:
        if error_occurs:
            print("Too bad.")
        else:
            print("YAY!")

raise_exception(25)
print("\n")

raise_exception(-1)
print("\n")

raise_exception(7j)

````
