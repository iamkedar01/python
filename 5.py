"""  list in python 8 
      list: its is collection of different datatype that is stored in in singele variable ,
            its is ordered,mutable(changeable),duplicate
        """
print("Details about the list...!")
print("Lists are orderd , mutable , allow duplicate elements")

fruits = ["apple", "banana", "cherry",]
print(fruits[0])  
print(fruits[2], end=" ") # it will not enter the  next line 
print(fruits[-1]) 
print(fruits[-2])  

l = [1 , 7 , 3 , 7 , 8 , 5 , 6 , 7 , 1 , 2 , 4 , 9.5 , 10.1]
"""""
print(l)
print(len(l))
print("Accesing the elements in list")
print(l[5])
print(l[-3])  # Accesing the elements in list """

print("modifing list")

# Adding the new elements 
fruits.insert(1, "orange")
print(fruits)
fruits.append("Lemon")
fruits.append("Mango")
print(f"{fruits}, Here add the two fruits")
print(f"{len(fruits)},It will count the total fruits")

# Removeing the elements in the list
fruits.remove("apple") 
print(f"{fruits},it will remove the mention elements")
fruits.pop()
print(f"{fruits},it will remove the  last elements")

# Slicing list
print("------------------------>slicing the list")
print(l[3:7]) # it eill not include the 7 index
print(l[7::]) # it will include the 7 index also.
l.sort()
print(l) # here we sort the list in ascending order 
print(l[0::2]) # above we sorted bcz next we get the even number only
# print(enumerate(l))

# Method and commen function
print(f"{l} ,Its is a normal list")
l.sort()
print(sorted(l))                                # both line 41 & 42 will give the same output
print( f"{l} , sorted list in ascending order")
l.reverse()
print(f"{l} list in descending order")
print(f"{l.count(7)} , it wil give the number time 7 will repeat")
print(f"{sum(l)} , it will total sum of list")

# nested lists it is widely used in the matrix

matrix = [
    [ 1 , 2 , 3 ],
    [ 4 , 5 , 6 ],
    [ 7 , 8 , 9 ]
]
print(matrix)
print(matrix[0])
print(f"{matrix[1]}, it will a particular list in the index ")
print(matrix[2][1])
print(f"{matrix[1][2]}, it is used to acces the element list inside the list ")
