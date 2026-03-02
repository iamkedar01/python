# Take inputs from the user in the from the floating points
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

# Calculate SI
si = (p * r * t) / 100 # calculate the SI useing the BADMASS formula

print("Simple Interest:", si)