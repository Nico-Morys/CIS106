itemprice = float(input("Enter the Price of the Item: $"))
discountpercent = float(input("Enter the Discount Percent as a decimal please: "))
discountamount = float(itemprice * discountpercent)
priceafterdiscount = float(itemprice - discountamount)

print("Amount that has been discounted: $",discountamount, "  Price after discount is: $",priceafterdiscount)