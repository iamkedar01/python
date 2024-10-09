#  tuples in python 
print("Tuples are ordered, immutable , similar to the list but can't modify """)
my_tuple = (1 , 2, 3 , 4 , 5, 10 , 9 , 8 , 7 , 6)
print(my_tuple)

# Acessing tuple in python 

boys = ("Mallu","Kedar","Manju","Pintu","Shree","siddu")
print(boys)

print("\n Using the for loop and fstring printing the name and index:")
for name  in boys:
    print(f"The name of the boys is :{name}") #it will simple print the names 
for name  in boys:
    print(f"The index of {name} is: {boys.index(name)}") # i = boys.index(name) then  print(i)
    # it will print the name with index

print("\n",boys[1])
print(boys[2])

print(f"{boys[0]} , is the big brother in our family")
print(f"{boys[-1]} , is the little brother in our family")
# Slicing
print(boys[3:len(boys)]) # it will print the end of the tuple
print(boys[2::]) # it will start printing the after second one 

# tuple opertion
# ---> tuple concatention 
t1 = (1 , 2, 3) 
t2 = (4, 5 , 6)
t = t1 + t2
print(f"{t} , It is the combination of two tuple")
r = t1  * 2
print(f"{r},it will repeate the multiple time by given value")
print("Kedar " not in boys)
print(f"{"kedar" in boys} --->python is case senstive ") # mean it will uppecase and lowercase letter will diffrent one

#it 