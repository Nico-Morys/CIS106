def comptotal(qty, price): 
    total = float(qty) * float(price)

    if total > 10000.00:
        total = total * .90
    else:
        total = total

    return total

qty = float(input("Please Enter a quantity: "))
price = float(input("Please Enter a price: "))

total = comptotal(qty, price)

print("The total is: ", total)