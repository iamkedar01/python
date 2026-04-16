text = input("Enter text: ")

freq = {}   # Empty dictionary

for ch in text:
    # If character already exists in dictionary
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequency:")
print(freq)