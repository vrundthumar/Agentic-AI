# Train Seats Information Provider

seat_type = input("Enter seat type (Ac/Sleeper/Luxury/General): ").upper()

match seat_type:
    case "AC":
        print("AC - It is most comfortable.")
    case "SLEEPER":
        print("Sleeper - It is comfortable but non-ac.")
    case "LUXURY":
        print("Luxury - it is non recliner.")
    case "GENERAL":
        print("General - It is less comfortable.")            
    case _:
        print("Invalid seat type.")    
 

# OUTPUT
# Enter seat type (Ac/Sleeper/Luxury/General): ac
# AC - It is most comfortable.
#  Enter seat type (Ac/Sleeper/Luxury/General): seater
# Invalid seat type.
