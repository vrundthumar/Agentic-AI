# Walrus Operator

# THIS IS BASIC LOGIC

# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")   OUTPUT : Not divisible, remainder is 3

# NOW BY USING WALRUS OPERATOR

value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}") 

# Not divisible, remainder is 3 

