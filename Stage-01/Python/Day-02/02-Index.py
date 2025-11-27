# Lists

fruits = ["Apple", "Banana", "Mango"]
# index     0         1         2 

# Printing element of list
print(fruits[0]) # Apple

# Changing Value
fruits[1] = "Orange"

# Adding elements
# At end

fruits.append("Graps")

# At a specific posion
fruits.insert(2, "Tomato")

# Deleting elements
# Delete specific element
fruits.remove("Apple")

# Delete the element using index
fruits.pop(1)


# Looping through a list

for x in fruits:
    print(x)

# Output 
# Apple
# Orange
# Mango
# Graps


# Length of list
print(len(fruits)) # 3