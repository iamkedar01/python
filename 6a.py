""" set opertion in python 
    set are the collection of unique items unorderd and unindexed 
     syntax: my_set = { element1, element2, element3, etc...} 
     it is also declare in the flower bracket    """

set1 = {1,2,3,3,4,5} 
set2 ={3,4,5,6,7}
set3 = set1 - set2 
print(f"the  diffrence of set1:{set1} and set2:{set2} is given by-->{set3 }")

Student_set = {"Manju","Mallu","Niranjan", "Shree","Siddu","unkown"}
print(type(Student_set))
print(Student_set)

# Set opertion in python
# union opertion symol is: |  and it will remve the similar elements in set both kept only one
set4 = set1 | set2 
print(set4)

## intersection opertion symbol is:& it will  returns elements that are common to both sets.

set5 = set1 & set2 
print(set5)

# set methods 1) add , 2) remove 3) discard , 4) clear  5) pop
# 1) add the element in a list 
Student_set.add("kedar")
print(Student_set)

# 2) remove the spcified element in a set 
Student_set.remove("unkown")
print(Student_set)

# 3) Discard it will remove the element & if element is not in set iw will genrate any eroor
Student_set.discard("Rocky")  
print(Student_set)

# 5) pop remove the random element in a set
Student_set.pop() 
print(Student_set)


# 4th is here is because we can't do pop opertion  
# 4) clear is used to delete all the elements in  set 
Student_set.clear()
print(Student_set)

''' A simple information about the set opertion and methods and set not in orderd '''