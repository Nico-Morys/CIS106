response = input("If you would like to continue enter Yes or No: ")
sum = 0

while response == "Yes":
    make = input("Please Enter the Make of the Vehicle: ")
    model = input("Please Enter the Model of the Vehicle: ")
    code = input("Please Enter The Electric Code Y or N: ")
    msrp = float(input("Please Enter the Sticker Price of the Vehicle: "))
    response = input("If you would like to continue enter Yes or No: ")

    def compmsrp(make, model, code, msrp):
        if make == "Honda" and model == "Accord":
            percent = .10
        elif make == "Toyota" and model == "Rav4":
            percent = .15
        elif code == "Y":
            percent = .30
        else: percent = .05

        discount = msrp * percent
        newmsrp = msrp - discount
        msrp1 = newmsrp * .07 
        finalmsrp = newmsrp + msrp1 

        return finalmsrp

    finalmsrp = compmsrp(make, model, code, msrp)

    sum = sum + finalmsrp 


print("Vehicles Total: ", finalmsrp)
print("Sum: ", sum)

