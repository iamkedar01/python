char = input("Enter a character: ")

# Convert to lowercase to handle uppercase inputs
char = char.lower()

if char in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")