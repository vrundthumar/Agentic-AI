# Palindrome checker
import string

user = input("Enter A Word: ")

antiuser = user[::-1]

if user == antiuser:
    print("It is Palindrome")
else:
    print("It is not an Palindrome")    

# OUTPUT
# Enter A Word: level
# It is Palindrome