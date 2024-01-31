partnum = int(input("Please Enter a Part Number: "))
quantity = float(input("Please Enter a Quantity: "))



if partnum == 10 or partnum == 55:
    unitcost = 1.00
elif partnum == 99:
    unitcost = 2
elif partnum == 80 or partnum == 70:
    unitcost = 3
else: unitcost = 5


totalcost = float(quantity) * unitcost

print("Part Number: ", partnum)
print("Cost Per Unit: ", unitcost, "Total is: ", totalcost)
