#input and output 
# Inside the print statement to print user given value 

name =  "Kedar"#input("Enter your name:")
Age = "Dhage" #int(input("Enter your age:"))
print(f"Hello , {name}! your age is : {Age} ") # using fstring to print

# String opertion and some slicing 
first_name = "Rocky" #input("Enter the First_name :") # give the input from the keyboard
last_name = "bhai" #input("Enter the Last_name: ") 
full_name = first_name + last_name + " "  # If you want space middle of  the fullname then add like this( +" "+ )
print(full_name) 
print(full_name * 3) # repition of the given message 
print(full_name.upper()) # converting into the uppercase to the given string 
print(full_name.lower()) # converting into the lowercase to the given string 
message ="            Hello , world...!    "
print(message)
print(message.strip()) # it will remove space in message text before text and after text insde the double ""
#print(message.count(message))/
print(message.replace("world","python")) # first it will replace then it will remove the space

# Accesing the string character 
text = "python"
print(text[0]) # which charcter is present in the index o
print(text[-2])
# slicing  opertion will start from here 
print("Slicing String")
text1 = "pythonprograming"
print(len(text1))
print(text1[7:]) # after the 7 index it will start printing 
print(text1[0:3]) # it will print the in b/t the 0 to 3 charcter includeing the 3
print(text1[6::2]) # To  print the words by missing one word one in given text 

#Escape Sequence 
print("Hello\tworld")
print("python\nproramming")
