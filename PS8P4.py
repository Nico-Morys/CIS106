response = input("Would you like to start? Please Enter Yes or No: ")
sum = 0

while response == "Yes":
    lastname = input("Please enter your last name: ")
    miles = float(input("Please Enter the distance to downtown Chicago in miles: "))


    def compprice(lastname, miles):
        if miles >= 30:
            ticketprice = 12
        elif miles >= 20:
            ticketprice = 10
        elif miles >= 10:
            ticketprice = 8
        elif miles < 10:
            ticketprice = 5

        return ticketprice
    ticketprice = compprice(lastname, miles)
    sum = sum + ticketprice
    response = input("Would you like to find the price of more tickets? Please Enter Yes or No: ")

print("Your Ticket Price is: ", ticketprice)
print("Sum is: " ,sum)