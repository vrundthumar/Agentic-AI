# USE OF BREAKING STATMENTS
flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} item found")

print("Out of loop")  

# OUTPUT
# Ginger item found
# Lemon item found
# Out of loop