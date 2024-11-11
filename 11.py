# List and Dictionary Comprehension using the for loop
# Comprehension mean easy to understand

# List Comprehension using the for loop

lists = [1,2,3,4,5,6,7,8,9,10]
# print(sum(lists)) --> simple we can do but here using the for loop
total =0
for num in lists:
    total += num #total = total + num 
print(f"Total sum of num is: {total}")

# Doubling each number in a list
numbers = [1, 2, 3, 4, 5]
doubled = [] # thsi one empty list 
for num in numbers:
    doubled.append(num * 2) # Here doubled value is append in double list
print("Doubled numbers List:", doubled)

foods = ["Dosa", "Idli", "Vada", "Roti"]
for food in foods:
    print(f"I like {food}")
else:
    print("All printed...!")
