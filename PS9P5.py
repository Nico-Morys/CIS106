quantity = float(input("Please Enter The Quantity: "))
unitprice = float(input("Please Enter The Unit Price: "))

def comp(quantity, unitprice): 
    global total
    global tax
    total = quantity * unitprice 
    tax = total * .07
    
    return total, tax

total, tax = comp(quantity, unitprice)

print("Total is: ", total)
print("Tax Amount is: ", tax)
