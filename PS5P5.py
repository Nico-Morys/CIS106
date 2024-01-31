response = input("Please Enter Yes or No: ")
discount1 = .25
discount2 = .10
discount3 = 0

while response == "Yes": 
    quantity = int(input("Please Enter a Quantity: "))
    priceofitem = float(input("Please Enter A Price of Item: "))
    extendedprice = quantity * priceofitem
    if extendedprice > 10000:
        discountamount = extendedprice * discount1
    elif extendedprice < 10000:
        discountamount = extendedprice * discount2
    totalprice = extendedprice - discountamount
    discount3 = discount3 + discountamount
    print("Extended Price: ", extendedprice)
    print("Discount Amount is: ", discountamount)
    print("Total Price is: ", totalprice)
    response = input("If you want to do this again please enter Yes or No: ")



print("Discounted Amount Total is: ", discount3)