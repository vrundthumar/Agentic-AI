menu = ["Cheese", "Mozerella Cheese", "Veg-Loded"]

# enumerate it is used to get no in list.
for index, name in enumerate(menu, start=1):
    print(f"{index} : {name} Pizza")


# OUTPUT
# 1 : Cheese Pizza
# 2 : Mozerella Cheese Pizza
# 3 : Veg-Loded Pizza
