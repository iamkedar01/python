# 5. Swap Two Numbers Without Third Variable 

a = int (input("Enter the first number:"))
b = int (input("Enter the Second number:"))

a , b  = b , a
# swaping the number useing the tuple 

print("After swapping:")
print("a =", a)
print("b =", b)