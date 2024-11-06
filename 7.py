''' Dictionary in the python : A dictionary in Python is a collection of key-value pairs. 
        you can retrieve or manipulate data using the key. Unlike lists and tuples, dictionaries are unordered and mutable (changeable)
  1) Creating a Dictionary 
  2) Accessing Dictionary Elements 
  3) Adding and Updating Dictionary Elements
  4) Removing Elements from a Dictionary
  5) Dictionary Method
  6) Dictionary Characteristics

'''

IPL_teams = {
    "RCB": ["Virat Kohli", "ABD","Faf du Plessis", "Glenn Maxwell"],
    "CSK": ["MS Dhoni", "Ravindra Jadeja", "Deepak Chahar"],
    "MI": ["Rohit Sharma", "Ishan Kishan", "Jasprit Bumrah"],
    "DC": ["David Warner", "Prithvi Shaw", "Axar Patel"]
}

karnataka_food = {
    "Bengaluru":"Dosa" , "Mysuru":"Mysore Pak" , "Mangaluru":"Fish dishs" , "Hubali":"Roti" , "Mandya":"chapati"
}
# Accessing the dictionary elements

print(karnataka_food["Hubali"])  # must be in double cote " "

# adding and updateing the dictionary 
# ----> Adding the new elements 
karnataka_food["kalaburagi"] = "chai"  # using the equal symbol
print(karnataka_food)
#------> updating the existing one values
karnataka_food["Mandya"]="Ragi mude"  #here check the key letter Because python is case sencitive
print(karnataka_food)


# Removing Elements from a Dictionary
# ----> pop(): removes the specified key and returns the associated value.
mysuru_food = karnataka_food.pop("Mysuru") # inside  the pop spcifies the key
print(mysuru_food)
# ----->del: Removes the specified key
del karnataka_food["Mangaluru"]
#------> clear(): Empties the dictionary
# karnataka_food.clear()  # make the comment off while using the code 

# Dictionary Methods 
# ---> keys(): it return the all the keys in dictionary 
print(karnataka_food.keys())
# ----> Values(): it retur the all the values in dictionary  
print(karnataka_food.values())
# ----> (Items(): it return the all the items in the dictionary
print(karnataka_food.items())

# a small question like using the list in dictionary 

team_name = input("Enter the IPL team name(only short fron in capital letter)----> ")
if team_name in IPL_teams:
    print(f"Players in {team_name}: {','.join(IPL_teams[team_name])}") # it is used to add the comma between each players
else:
    print("This team is not in the IPL_teams dictionary.")

# this above question about cricket teams 
# you make the similar like nation respctive states, states contain the famous citys
# and family family family_headname  and their family_members etc