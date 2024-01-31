lastname = input("Please Enter A Last Name: ")
numdependents = int(input("Please Enter The Number Of Dependents: "))
grossincome = float(input("Please Enter Your Gross Income: "))
adjustedgross = grossincome - (numdependents * 12000)
taxrate1 = .20 
taxrate2 = .10
taxrate3 = 100

if adjustedgross > 50000:
    incometax = adjustedgross * taxrate1
    if incometax < 0: 
        print(lastname, grossincome, numdependents, adjustedgross, taxrate3)
    if incometax >= 0:
        print(lastname, grossincome, numdependents, adjustedgross, incometax)
elif adjustedgross <= 50000: 
    incometax = adjustedgross * taxrate2
    if incometax < 0: 
        print(lastname, grossincome, numdependents, adjustedgross, taxrate3)
    if incometax >= 0:
        print(lastname, grossincome, numdependents, adjustedgross, incometax)



        


