numbers = [10, 20, 4, 45, 99]

# Remove duplicates first (optional but good practice)
numbers = list(set(numbers))

numbers.sort()

# Second largest is second last element
print("Second Largest:", numbers[-2])