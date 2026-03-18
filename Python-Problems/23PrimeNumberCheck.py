num = int(input("Enter a number: "))

# Prime number must be greater than 1
if num <= 1:
    print("Not Prime")
else:
    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        # This else belongs to for loop
        print("Prime Number")