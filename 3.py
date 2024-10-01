#input and output 
# Inside the print statement to print user given value 
name =  "Kedar"#input("Enter your name:")
Age = "Dhage" #int(input("Enter your age:"))
print(f"Hello , {name}! your age is : {Age} ")

# String opertion and some slicing 
first_name = "Rocky" #input("Enter the First_name :") # give the input from the keyboard
last_name = "bhai" #input("Enter the Last_name: ") 
full_name = first_name + last_name + " "  # If you want space middle of  the fullname then add like this( +" "+ )
print(full_name)
print(full_name * 3)
print(full_name.upper())
print(full_name.lower())
message ="            Hello , world...!    "
print(message)
print(message.strip()) # it will remove space in message text before text and after text insde the double ""
#print(message.count(message))/
print(message.replace("world","python")) # first it will replace then it will remove the space

# Accesing the string character 
text = "python"
print(text[0])
print(text[-2])

print("Slicing String")
text1 = "pythonprograming"
print(len(text1))
print(text1[7:])
print(text1[0:3])
print(text1[6::2]) # To  print the words by missing one word one in given text 

#Escape Sequence 
print("Hello\tworld")
print("python\nproramming")
