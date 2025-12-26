# Global scope

chai_type = "Plain"

def front_desk():

    def kitchen():
        global chai_type # it will change every where chau type to irani in the code.
        chai_type = "Irani"

    kitchen()

front_desk()
print("Global chai type : ", chai_type)    

# Output
# Global chai type :  Irani
