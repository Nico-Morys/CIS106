item = (input("Please Enter an Item A or B: "))
quantity = (float(input("Please Enter a Quantity: ")))

if item == "A":
    unitprice = (10)
elif item == "B":
    unitprice = (20)

extendedprice = quantity * unitprice

print("Item: ",item)
print("Unit Price: $",unitprice ,"Extended Price is: $",extendedprice)