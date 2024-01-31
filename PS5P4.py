response = input("Please answer Yes or No if you want to calculate gross pay: ")
count = 0
rop1 = 0
grosspay1 = 0

while response == "Yes":
    count = count + 1
    lastname = input("Please Enter A Last Name: ")
    hours = float(input("Please Enter the amount of hours worked: "))
    rop = float(input("Please enter the rate of pay: "))
    if hours > 40:
        timeandahalf = (hours - 40) * (rop * 1.5)
        grosspay = hours * rop
        finalpay = grosspay + timeandahalf
    elif hours <= 40:
        grosspay = hours * rop
        finalpay = grosspay 
    print(lastname, " Gross Pay is: ", finalpay)
    rop1 = rop1 + rop
    grosspay1 = grosspay1 + finalpay
    response = input("If you want to compute gross pay again please enter Yes or No: ")

print("Gross Amount Payed ", grosspay1, "Employees: ", count)

averagepay = rop1 / count

print("Average Pay is: ", averagepay)