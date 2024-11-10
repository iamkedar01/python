''' for  loop in python 
A for loop allows you to repeat a block of code a fixed number of times,
 or once for each element in a sequence.
'''
#for item in sequence:
    # Code to execute for each item in the sequence

# using the for loop 

cities = ["kalaburagi", "Bengaluru","Hubballi","mysore","Mandya","bidar"]
for city in cities:
    print(city, end = " ")
print()
# using the range() function with for loops 
'''The range() function generates a sequence of numbers, 
which you can use in a for loop when you want to repeat a block of code a specific number of times'''

# pritning the 1 to 10 sequence number using range fuction 
for num in range(1,11):
    print(num, end= "  ")
print() # this is used to skip the continue printing


# here we using the step operation in range 
for num in range (1,11,2):
    print(num,end="     ")  #In end we give three tab space in output you can see difference 
print()

# looping over string 
name = "Kalaburagi"
for letter in name:
    print(letter) # here also we can use the end to print Horizontal 
print()

# nested for loops
'''You can also have nested for loops, which means a loop inside another loop.
 This is useful when working with multi-level data, like lists inside lists.'''
 # using the nested for printing the multiplication table
for i in range(1,11):# for normmal printing i=(1,11) and j=(1,5) for vertical retrun code 
    for j in range(1,5): #In both i and j th range values also we need to change  
        print(f"{i} x {j} ={i*j}", end ="\t") # here (end="\t") is used to print the vertical line |
    print() # it is used move the next line after every jth iteration 
print()


# In for also uesd the continue and break statement 

#--->continue is used to skip the spcific step 
for city in cities:
    if city == "Hubballi":
        continue
    print(city)
print("\n")


#---> Break statement is used stop iteration 
for city in cities:
    if city == "Hubballi":
        print(f"Found {city}!")
        break
    print(city)
print("\n")


#----> Looping Through a List with enumerate()
# is is used to over a sequence get both index and values in list
for index, city in enumerate(cities):
    print(f"city:{index+1} = {city}") # index+1 is because evey index start with 0
print()


#---> using the else case in for loop 
for i in cities:
    print(i)
else:
    print(" All cities are printed..!") # it is mostly used in the brake and continue  statement
