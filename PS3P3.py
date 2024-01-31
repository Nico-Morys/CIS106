bookquantity = (int(input("Please Enter The Amount of Books: ")))
cpb = (float(input("Please Enter The Cost Per Book: ")))
shippingfee = (25)
shippingfee2 = (0)
ordertotal = cpb * bookquantity
finalamount = ordertotal + shippingfee

if ordertotal <= 50:
    finalamount = ordertotal + shippingfee
    print("Order Total is: $", finalamount, "Shipping Fee is: $", shippingfee)
elif ordertotal > 50:
    finalamount = ordertotal 
    print("Order Total is: $", finalamount, "Shipping Fee is: $", shippingfee2)


