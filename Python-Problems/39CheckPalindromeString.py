text = input("Enter a string: ")

# Reverse string
reverse = text[::-1]

# Compare original and reversed
if text == reverse:
    print("Palindrome String")
else:
    print("Not Palindrome")