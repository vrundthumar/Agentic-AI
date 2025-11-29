# Delivery charge calculator

total = int(input("Enter amount: "))

if total < 100:
    total = total + 29
else:
    total = total + 0

print(f"The total amount to pay after all the charges is: {total}")        

# Output
# Enter amount: 200
# The total amount to pay after all the charges is: 200

# Enter amount: 99
# The total amount to pay after all the charges is: 128