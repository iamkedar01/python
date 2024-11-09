'''             While Loops in Python
A loop is a programming structure that repeats a set of instructions as long as a specified condition is True. 
In Python, the while loop allows you to repeatedly execute a block of code as long as the condition is True.     '''
# Syntax:---->
# while condition:
    # Code to execute as long as condition is True
    # here we can make the increment or decrement based on usage

# using the whle loop printing the 1 to 7 number 
num = 1
while num < 8:
    print(num , end=" ")  # here end use to stoop the entering the new line 
    num += 1
print()
# here using the num printing the even number 
i = 1
while i <= 20 :
    if i % 2 ==0:
     print(f"The even number is:{i}")
    i +=1
# using the brake statement in the while loop
sheep_count = 1
while sheep_count <= 10:
    print(f"Sheep {sheep_count}")
    if sheep_count == 5:
        print("That's enough counting!")
        break # it work bassed on the if condition 
    sheep_count += 1

# using the continue statement 
bus_count =1
while bus_count <=5:
    if bus_count ==2:
        bus_count+=1 # here we need to increment bcz it satisafied the condition. it wil stop 
        continue
    print(f"Bus NO is:{bus_count}")
    bus_count+=1 # this for whole step after that condition 

# To user for a PIN until they enter the correct one:

pin = ""
correct_pin = "137"
attempts = 0
while pin != correct_pin and attempts < 3:
    pin = input("Enter your PIN: ")
    if pin != correct_pin:
        attempts+=1
        print(f"Incorrect PIN. Try again.{3 - attempts} only attemptes are left")
if(pin == correct_pin):
    print("PIN accepted. You can proceed.")
else:
    print("Too many attempts. Access denied..!")

