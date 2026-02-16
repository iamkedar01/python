 # 1. Print “Hello, World!”
print("Hello world")
# here we useing the  print built in function to display the message to the user 

# 2. Take Two Numbers from the user and Print Their Sum

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the Second number:"))

# here we takeing the two number from the user 

sum = num1 + num2

print("The sum of the", num1," and " ,num2, " is :",sum)

# here the another way of the writeing the print statement 
# this is called the Fstring method 
print(f"The sum of the {num1} and {num2} is :{sum}")
