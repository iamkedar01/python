num = int(input("Enter a number: "))

original = num
reverse = 0

# Reverse number
while num > 0:
    digit = num % 10        # Get last digit
    reverse = reverse * 10 + digit
    num = num // 10         # Remove last digit

# Compare
if original == reverse:
    print("Palindrome Number")
else:
    print("Not Palindrome")