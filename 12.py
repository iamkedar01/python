# Function 
''' A function is a reusable block of code that performs a specific task when called.
 Functions are useful to organize code, make it reusable, and reduce redundancy. '''

# Defining a Function 
# You define a function using the def keyword followed by the function name, parentheses, and a colon :.
''' Syntax-->
           def function_name(parameters):
                # Block of code   '''
#Function Parameters 
# parameters are variables used to pass data into a function 

#Example: Basic function to greet a user
def greet():
    print("Hello! Welcome to the Python course.")
greet() # used to call the function 

# Function parameters
# parameters are used to  pass data into a function 
def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python course.")
greet_user(input("Enter your name:")) # asking the user to enter the name

# Returning Values from a Function
""" A function can return a value using the return keyword, which 
allows the output of the function to be reused elsewhere. """
# Function that adds two numbers and returns the result
def addition_of_two_number (a, b):
    result = a+b
    return f"the sum of two number is: {result}" # it will return result in this statement
a = int(input("Enter first number: "))
b = int(input("Enter second number:"))
print(addition_of_two_number(a,b)) #return value must be printed using the function name and parameter

# Default Parameter Values
"""You can define a default value for a parameter, 
which is used if no argument is passed when the function is called."""
# Example: Function with a default parameter
def greet(name="Student"):
    print(f"Hello, {name}! Welcome to the Python course.")
greet()  # Uses default value "Student"
greet("Geetha")  # Uses passed value "Geetha"
# Here value is not passed by the input
""" Local and Global Variables
Local Variables are defined inside a function and are only accessible within that function.
Global Variables are defined outside all functions and are accessible from anywhere in the code."""

name = "Global Name"
def greet():
    name = "Local Name"
    print(name)
greet()  # Prints local variable
print(name)  # Prints global variable