# Powerful Password generator

import random

random.seed(10)
password = ''
for i in range(8):
    password += (chr(random.randint(64, 123)))

print(f"The Random Generated password 🔐: {password}")    

# OUTPUT
# The Random Generated password 🔐: dB[^d@M]