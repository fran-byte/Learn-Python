:page_with_curl: [README](../README.md) :pencil: [Exercises](/tests/indicetests.md)

# 8. ITERATIVE STATEMENTS (LOOPS)

## while

````python
c = 0
while c <= 5 : # It will be executed while c is less than or equal to 5

print("c equals: ",c)
c+=1
print ("The loop has ended")
`````

>c equals: 0
>
>c equals: 1
>
>c equals: 2
>
>c equals: 3
>
>c equals: 4
>
>c equals: 5
>
>The loop has ended

## while True:
## Building an Infinite Loop

````python

while True : # It will be executed will always run until interrupted by the sentence (break)

print("""OPTIONS
1- GREET
2- ADD 2 Numbers
3- EXIT""")
option=input()

if option == "1":
print("HELLO")

elif option == "2":
n1=float(input("N.1: "))
n2=float(input("N.2: "))
print(n1,"+",n2,"=",n1+n2)

elif option == "3":
print("PROGRAM COMPLETED !!")
break # Here we break the loop

else:
print("Invalid option, try again")

print("We are out of the while True (Infinite Loop)")
`````
