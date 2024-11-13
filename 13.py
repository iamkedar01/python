# Function - Advanced Concets
"""explore more advanced function concepts, including recursion,
 lambda functions, and variable-length arguments. """

# 1.keyword Aruguments
"""With keyword arguments,
 you can pass values to a function by specifying the parameter names."""

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")
display_info(age=25, name="Kumar")

# 2. Variable-Length Arguments
# You can use *args and **kwargs to accept a variable number of arguments in a function.
# usinng the *args
def total_sum(*numbers): #Enter the  more then numbers
    result = 0
    for num in numbers:
        result += num
    return result
print(total_sum(1, 2, 3, 4))

# using the **kwargs
def student_info(**details):  #give the key value in parameters
    for key, value in details.items():
        print(f"{key}: {value}")
student_info(name="Anand", age=22, course="Python")
 
#3. Lambda Functions
"""A lambda function is a small anonymous function that
 can take any number of arguments but has only one expression. """
# lambda arguments: expression
double = lambda x: x * 2
print(double(5))

#4.Recursion
"""Recursion occurs when a function calls itself.
 It's used to solve problems that can be broken down into smaller, similar problems."""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
