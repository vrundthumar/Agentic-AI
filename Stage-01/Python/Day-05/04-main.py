def cafe():
    coffee_type = "Mocha"

    def inside_cafe():
        nonlocal coffee_type # you can use outside this function but not globally.
        coffee_type = "Latte"

    inside_cafe()
    print(f"after inside cafe update : {coffee_type}")


cafe()
# output
# after inside cafe update : Latte
