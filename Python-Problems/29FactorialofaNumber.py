num = int(input("Enter a number: "))

factorial = 1  # Initial value must be 1

# Multiply numbers from 1 to num
for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial is:", factorial)