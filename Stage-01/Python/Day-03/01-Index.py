# Dictionary
car = dict(type="Hyper car", prise = "$50000")
print(car) # {'type': 'Hyper car', 'prise': '$50000'}

coffee = {}
coffee["Name"] = "Cold coffee"
coffee["Size"] = "Tall"
coffee["Sweat type"] = "Honey"

print(coffee) # {'Name': 'Cold coffee', 'Size': 'Tall', 'Sweat type': 'Honey'}

del coffee["Sweat type"] # To delete element from Dictionary
print(coffee) #{'Name': 'Cold coffee', 'Size': 'Tall'}

print(f"Is the coffee sweat ? {"Sweat type" in coffee}") # Membership Testing
# Is the coffee sweat ? False

print(f"Item keys: {coffee.keys()}")  # Item keys: dict_keys(['Name', 'Size'])

print(f"item values: {coffee.values()}")  # item values: dict_values(['Cold coffee', 'Tall'])

print(f"the last item: {coffee.popitem()}")  # the last item: ('Size', 'Tall')
