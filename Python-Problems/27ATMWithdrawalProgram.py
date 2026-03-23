balance = 10000  # Assume fixed balance

amount = float(input("Enter withdrawal amount: "))

# Check sufficient balance
if amount <= balance:
    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")