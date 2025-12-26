# Scopes

def serve_chai():
    chai_type = "Ginger"  # local scope -->  it can not be accesed outside the function
    print(f"Inner : {chai_type}")

serve_chai()

chai_type = "Lemon"
print(f"Outer : {chai_type}")

# Output
# Inner : Ginger
# Outer : Lemon



def chai_counter():
    chai_order = "Lemon" # Enclosing scope
    def print_order():
        chai_type = "Ginger"
        print(f"Inner : {chai_type}")
    print_order()
    print(f"outside : {chai_order}")


chai_counter()

chai_type = "Tulsi" # Global Scope --> it can be accesed anywhere in the code
print(f"Global : {chai_type}") 

# Output
# Inner : Ginger
# outside : Lemon
# Global : Tulsi