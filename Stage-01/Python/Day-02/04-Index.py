# Sets
# It cannot have duplicate value
# its order is not fixed

cars = {"BMW", "Audi", "Pagani"}


numbers = {1, 2, 3, 2, 4, 4}
print(numbers)  # {1, 2, 3, 4}

# How tp add element in to sets
cars.add("Bugati")
numbers.add(5)

# How to remove element
cars.remove("Audi")

all = cars | numbers # | = Pipe operator
print(all) # {1, 2, 'Bugati', 'Pagani', 3, 4, 5, 'BMW'}
