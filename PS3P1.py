quantity = float(input("Enter A Quantity: "))
tax = float(.07)

if quantity >= 1000:
    UnitPrice = (3)
    extendedprice = quantity * UnitPrice
elif quantity < 1000:
    UnitPrice = (5)
    extendedprice = quantity * UnitPrice


taxamount = extendedprice * tax

total = taxamount + extendedprice


print("Quantity is:",quantity)

print("Unit Price is: $",UnitPrice, "Extended Price is: $",extendedprice, "Tax Amount is: $",taxamount, "Total Cost is: $",total)