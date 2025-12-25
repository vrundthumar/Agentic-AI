# For Else loop
staff = [("Amit", 16), ("Zara", 17), ("Alex", 15)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage office.")
        break
else:
    print("No one is eligible to manage the office.")    


# OUTPUT
# No one is eligible to manage the office.