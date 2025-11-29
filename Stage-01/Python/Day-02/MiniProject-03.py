# Palindrome

word = str(input("Enter a word: "))

palidrome = word[::-1]

if word == palidrome:
    print(f"The word you given is palindrome")
else:
    print(f"The word you given is not palindrome")


# Output
# Enter a word: vrund
# The word you given is not palindrome 