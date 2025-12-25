# CAFE Bill Calculator

cups_input = int(input("Enter no of cups: "))
size_input = input("Enter the size of cup(Small/Medium/Large): ").lower()

def gst_calculator(value):
    return (value * 5) / 100

def calculate_bill(cups, size):
    if size == "small":
        amount = cups * 15
        gst = gst_calculator(amount)
        total = amount + gst
        print(f"Amount(Without Tax): {amount}")
        print(f"Amount Including GST: {total}")

    elif size == "medium":
        amount = cups * 25
        gst = gst_calculator(amount)
        total = amount + gst
        print(f"Amount(Without Tax): {amount}")
        print(f"Amount Including GST: {total}")

    elif size == "large":
        amount = cups * 30
        gst = gst_calculator(amount)
        total = amount + gst
        print(f"Amount(Without TAX): {amount}")
        print(f"Amount Including GST: {total}")

    else:
        print("Invalid amount of cups or size of cup")    


calculate_bill(cups_input, size_input)  

# OUTPUT
# Enter no of cups: 4
# Enter the size of cup(Small/Medium/Large): large
# Amount(Without Tax): 120
# Amount Including GST: 126.0


