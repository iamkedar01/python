text = input("Enter a string: ")

reverse = ""

# Loop through each character
for ch in text:
    reverse = ch + reverse   # Add character at beginning

print("Reversed string:", reverse)