numbers = [5, 2, 9, 1, 7]

largest = numbers[0]   # Assume first element is largest
smallest = numbers[0]  # Assume first element is smallest

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)