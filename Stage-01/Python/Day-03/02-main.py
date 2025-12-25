# Random Module
import random

print(random.random())  # 0.3098283227689451


dice = random.randint(1, 6)
print(dice)  # 4

random.seed(10) # on using seed the only one time random number will be selested than this will remain same on multiple times if we run the python file.
print(random.randint(1, 100)) # 74

