num = int(input("Enter a number: "))

original = num
result = 0

# Count digits
digits = len(str(num))

while num > 0:
    digit = num % 10
    result += digit ** digits
    num = num // 10

if original == result:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")