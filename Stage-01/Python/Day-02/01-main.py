# Functions

def greet():
    print("Hello")

greet() # Calling Function


def welcome(name):
    print("Welcome", name)

welcome("vrund") # Welcome vrund 


def sum(a, b):
    print(a + b)

sum(1, 4) # 5   


def square(num):
    return num * num

print(square(5)) # 25


def cheker(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")    


cheker(3) # Odd        