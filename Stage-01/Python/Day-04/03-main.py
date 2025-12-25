# Problem : The temperature should be increase by 15 until it reaches 100 and also starts with 40 and at every stage the temperature is to be printed.
temperature = 40

while temperature <= 100:
    print(f"Current Temperature {temperature}")
    temperature += 15

print("The tea is ready to serve")

# OUTPUT
# Current Temperature 40
# Current Temperature 55
# Current Temperature 70
# Current Temperature 85
# Current Temperature 100
# The tea is ready to serve