"""
Python Intro
------------

What is Python?
        Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.
Python is a general Purpose high-level interpreted language with easy syntax and dynamic semantics.
It is used for:
    web development (server-side),
    software development,
    mathematics,
    system scripting.

What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.

Why Python?
Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax similar to the English language.
Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
Python can be treated in a procedural way, an object-oriented way or a functional way.

Features of Python or Why is python popular?
    • Easy.
    • Free.
    • Simplicity.
    • Open-source.
    • Interpreted and platform-independent.
    • Very easy to debugging.
    • Provides very big library support.
    
what to you learn about the process of running the python program?
        whenever we run the program it first interprets, interpreter is there which use to interpret the python program basically the difference b/w the compiler and interpreter is nothing but compiler just complies the code all at one time but interpreter checks the code line by line.

Good to know!
        The most recent major version of Python is Python 3, which we shall be using in this tutorial. However, Python 2, although not being updated with anything other than security updates, is still quite popular.
In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.

Python Syntax compared to other programming languages!
Python was designed for readability, and has some similarities to the English language with influence from mathematics.
Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

Python Syntax
-------------

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
"""This is a comment written in more than just one line"""
print("Hello, World!")
"""
