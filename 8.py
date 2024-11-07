''' Conditional Statements in Python: if, elif, and else
    if-----> The if statement is used to test a condition. If the condition is True, the block of code under the if statement is executed.
    elif---> The else statement provides an alternative block of code to execute when the if condition is False
    else---> The elif statement checks another condition if the previous if or elif condition was False

    here uisng the camparision and logical opertions
    camparision opertions:(==:Equal to, !=:Not equal to,<:Less than,>:Greater than, <=:Less than or equal to,>=:Greater than or equal to )
    logical opertions:(and:Returns True if both conditions are True, or:Returns True if at least one condition is True, not:Reverses the result of a condition)
    
                                                                    '''

# ----> if condition
time = int(input("Enter the time: "))

if time == 8:
    print(" It is a dinner time ")

#-----> else conditon 
else:
    print(f"{time}, is not a dinner time")

#  useing the if , else ,and elif craete meals timeing 

time = int(input("Enter the time check the meals timeing: "))
if time == 7 or time ==8:
    print(f"{time},AM is brakefast time")
elif time == 1 or time == 2:
    print(f"{time},PM is lunch time")
elif time == 9:
    print(f"{time},PM is dinner time")
else:
    print(f"{time},is not a meal time..!")

# Checking Bus Ticket Prices based on the Age of passenger

age = int(input("Enter your age: "))
if age < 5:
    print("Ticket is free.")
elif age <= 12:
    print("You get a child discount.")
elif age >= 60:
    print("You get a senior citizen discount.")
else:
    print("You pay the full fare.")

# Nested if condition 
day = "Saturday"
is_raining = False # if raining enter the True boolean firs letter must be in capitial letter
if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")