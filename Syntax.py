"""
what is Python Syntax?
        Syntax is the arrangement of words and phrases to create well-formed sentences in a language.
Syntax Types:
        Execute Python Syntax
        Python Indentation
        Python Variables
        Python Comments

what is Execute Python Syntax?
        Execute Python syntax can be executed by writing directly in the Command Line:
Example
>>> print ('Hello, World!')
Hello, World!
Or by creating a python file on the server, using the .py file extension, and running it in the Command Line:
Example
arun@linux:~/path/to/code/location$ python3 PythonNotes.py
Hello, World!

what is Python Indentation?
        Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
Python uses indentation to indicate a block of code.
Example
if 5 > 2:
 print ("Five is greater than two")

Python will give you an error if you skip the indentation:
Example
Syntax Error:
if 5 > 2:
print ("Five is greater than two")

The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
Example
if 5 > 2:
 print ("Five is greater than two")
if 5 > 2:
    print ("Five is greater than two")

You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
Example
Syntax Error:
if 5 > 2:
 print ("Five is greater than two")
    print ("Five is greater than two")

What is Python Variables?
        Variables is a reserved memory location to store values.
Variable Types:
        n..,-2,-1,0,-1,2,..n    is a Integer
        a-z or A-Z              is a String
        Container name = Variable Name
        Storage container = Variable
        Underscore Character is a Variable
Example
Variables in Python:
x = 5                 # x is a Variable name        5 is a Variable
y = "Hello, World!"   # y is a Variable name        "Hello, World!" is a Variable
print (x)
print (y)

What is Python Comments?
        Python has commenting capability for the purpose of in-code documentation.
Comments can be used to explain Python code.
Comments can be used to make the code more readable.
Comments can be used to prevent execution when testing code.
Comments Types:
        Singleline Comments
        Multiline Comments

Singleline Comments
Comments start with a #, and Python will render the rest of the line as a comment:
Example
Comments in Python:
#This is a comment.
print("Hello, World!")

Comments can be placed at the end of a line, and Python will ignore the rest of the line:
Example
print("Hello, World!") #This is a comment.

A comment does not have to be text that explains the code, it can also be used to prevent Python from executing code:
Example
#print("Hello, World!")
print("Cheers, Mate!")

Multiline Comments
        Python does not really have a syntax for multiline comments.
Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:
Example
Reference from Comments.py"""
print ("Syntax Notes")
