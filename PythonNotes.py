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

Python Variables
----------------

What is Python Variables?
        Variables are containers for storing data values or Variables is a reserved memory location to store values.
Creating Variables:
        Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
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

Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type integer
x = "Sally" # x is now of type string
print(x)

What is Casting?
        If you want to specify the data type of a variable, this can be done with casting.
Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print (x)
print (y)
print (z)

Get the Type
        You can get the data type of a variable with the type() function.
Example
x = 5
y = "John"
print(type(x))
print(type(y))

What is Single or Double Quotes?
        String variables can be declared either by using single or double quotes:
Example
x = "John"
# is the same as
y = 'John'
print (x)
print (y)

Case-Sensitive
        Variable names are case-sensitive.
Example
This will create two variables:
a = 4
A = "Sally"
#A will not overwrite a
print (a)
print (A)

What is Python - Variable Names?
Variable Names
        A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
        A variable name must start with a letter or the underscore character
        A variable name cannot start with a number
        A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        Variable names are case-sensitive (age, Age and AGE are three different variables)
        A variable name cannot be any of the Python keywords.
Example
Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Example
Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

What is Multi Words Variable Names?
        Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:
        Camel Case
        Pascal Case
        Snake Case

Camel Case
Each word, except the first, starts with a capital letter:
Example
myVariableName = "John"

Pascal Case
Each word starts with a capital letter:
Example
MyVariableName = "John"

Snake Case
Each word is separated by an underscore character:
Example
my_variable_name = "John"

What is Python Variables - Assign Multiple Values?
        Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

Note: Make sure the number of variables matches the number of values, or else you will get an error.

One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
Example
x = y = z = "Orange"
print(x)
print(y)
print(z)

Unpack a Collection
        If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
Example
Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

What is Python - Output Variables?
        The Python print() function is often used to output variables.
Example
x = "Python is awesome"
print(x)

In the print() function, you output multiple variables, separated by a comma:
Example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

You can also use the + operator to output multiple variables:
Example
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

For numbers, the + character works as a mathematical operator:
Example
x = 5
y = 10
print(x + y)

In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
Example
Syntax error:
x = 5
y = "John"
print(x + y)

The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
Example
x = 5
y = "John"
print(x, y)

What is Python - Global Variables?
        Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
Example
Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
Example
Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

The global Keyword
        Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
Example
If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

Also, use the global keyword if you want to change a global variable inside a function.
Example
To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

Python Comments
---------------

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
Reference from Comments.py


"""
