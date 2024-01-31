quantity = float(input("Please Enter a Quantity: "))
price = float(input("Please Enter The Price: "))
discountrate = float(input("Enter The Discount Rate: "))


def compdiscount(price, discountrate):
    price1 = quantity * price
    discountamount = price1 * discountrate
    newprice = price1 - discountamount

    return (discountamount, newprice)

discountamount, newprice = compdiscount(price, discountrate)

print("Discounted Amount is: $", discountamount, "The New Price is: $", newprice)
