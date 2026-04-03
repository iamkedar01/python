# Take string input
text = input("Enter a string: ")

# Convert to lowercase to handle uppercase vowels
text = text.lower()

count = 0

# Loop through each character
for ch in text:
    # Check if character is vowel
    if ch in "aeiou":
        count += 1

print("Total vowels:", count)