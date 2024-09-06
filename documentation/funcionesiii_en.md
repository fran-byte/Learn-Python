:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

# 19. FUNCTIONS III
## RECURSIVE Functions (NON-RETURN)
They are used to subdivide the code into simpler tasks.
They are functions that call themselves. They have a certain resemblance to a loop or iteration.

````python
def counter(number):
    number *= 2
    if number <100:
        print(number)
        counter(number)
    else:
        print("number exceeded 100, we missed ", number)
        
    

counter(2)
````
## RECURSIVE Functions (WITH RETURN)

We can do an exercise to show the factorial of a number.

````python
def factorial(num):
    print("Initial value ->",num)
    if num > 1:
        num = num * factorial(num -1)
    print("final value ->",num)
    return num

print(factorial(5))

````

>Initial value -> 5  
Initial value -> 4  
Initial value -> 3  
Initial value -> 2  
Initial value -> 1  
final value -> 1  
final value -> 2  
final value -> 6  
final value -> 24  
final value -> 120  
120
