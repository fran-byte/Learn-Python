:page_with_curl: [README](../README_en.md) :pencil: [Exercises](/tests/indicetests.md)

#15. Inputs from the SCRIPTS terminal 
## import sys / sys.argv

Not everything is going to be writing code in the interpreter, 
Computer programs work differently. Files are created with instructions and these are called scripts (or instruction scripts). 
We send that file to the interpreter from the terminal (since python is an interpreted language), and it will be executed.  

And also these Scripts can receive data from the terminal at the time of execution.

Let's look at an example:

````python
import sys
if len(sys.argv)==3:
    text = sys.argv[1] # we introduce the argument 1 typed by terminal into the variable text
    repetitions = int (sys.argv[2]) # we introduce the argument 2 typed by terminal into the repetitions variable
                                        # and convert it to integer.
    for i in range(repetitions):
        print(text)

else:
    print("Error in arguments")
    print("name.py 'text' number of repetitions")
````

````shell script
C:\Users\franc\Desktop>script1.py hello 6
hello
hello
hello
hello
hello
hello

````
See this execution by terminal:

>script1.py hello 6

It has 3 arguments  

Argument[0] which is the file name: script1.py  

Argument[1] 'hello'  

Argument[2] 6
