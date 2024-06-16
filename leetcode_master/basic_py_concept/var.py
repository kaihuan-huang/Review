#Variables
# Variables are dynamicly typed
'''Questions on Variables and Dynamic Typing
Basic Variable Assignment and Types

1.What is dynamic typing, and how does Python implement it?
Create a variable named my_var and assign it the integer value 10. On the next line, reassign my_var to a string containing the text "Python". What does this demonstrate about Python's type system?
Type Checking

2.How can you check the type of a variable in Python? Provide a code snippet that checks the type of a variable named data and prints the type.
Type Conversion

3.Given a string variable str_number with value "1234", convert it into an integer and assign it to a new variable int_number. Write the Python code to do this.
'''
my_var = 10
my_var = "Python"
print(type(my_var))

str_number = "1234"
int_number = int(str_number)
print(int_number)

# Multiple assignments
'''Questions on Multiple Assignments
Simultaneous Variable Assignments

1. Python allows assigning values to multiple variables in one line. Assign the values 1, 2, and 3 to variables a, b, and c respectively in a single line of code.
Swapping Variables

2. Demonstrate how to swap the values of two variables x and y in a single line of code.'''


a, b, c = 1, 2, 3
print(a, b, c)

x = 5
y = 10
x, y = y, x  # Swapping x, y = y, x

# Increment
'''Questions on Increment Operations
Incrementing Variables

Given a variable counter initialized with the value 0, write a Python statement to increment its value by 5 using the += operator.
Decrementing Variables

Similar to the above, given a variable countdown initialized with the value 10, write a Python statement to decrement its value by 1.'''
a += 5
print(a)

b -= 1
print(b)

# None is null (absence of value)
'''Questions on None
Understanding None

What is the purpose of the None keyword in Python? Give an example of a situation where you might use None.
Checking for None

Write a Python function named is_none that takes a single argument and returns True if the argument is None, and False otherwise.
Optional Parameters with None

Write a Python function named greet that takes two parameters: name and greeting where greeting is optional and defaults to None. If greeting is None, the function should print "Hello, [name]!", otherwise, it should print "[greeting], [name]!".'''


n = None
print(n is None)

def is_none(n):
    if n is None:
        return True,
    else: 
        return False
    
print(is_none)


def greet(name, greeting=None):
    if greeting is None:
        print(f"Hello, {name}!")
    else:
        print(f"{greeting}, {name}!")
