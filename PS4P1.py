quantity = float(input("Please Enter A Quantity: "))
tax = .07

if quantity > 10000:
    price = 10
elif quantity > 5000:
    price = 20
elif quantity < 5000:
    price = 30

totalamount = quantity * price
taxamount = totalamount * tax
finalamount = totalamount + taxamount

print("Total is: ", finalamount)
print("Extended Price is: ", totalamount, "Tax Amount is: ", taxamount)
