salesperson = input("Please Enter The Salesperson Last Name: ")
sales = float(input("Please Enter The Amount in Sales: "))

def compcom(sales): 
    if sales >= 100000:
        commission = sales * .10
    else: commission = sales * .05

    target = sales * .05

    return commission, target

    
commission, target = compcom(sales)

print("Their Commission is: $", commission)
print("Next Year Target is: $", target)