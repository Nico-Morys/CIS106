numoftickets = int(input("Please Enter The Number Of Concert Tickets: "))

if numoftickets >= 25:
    priceperticket = 50
elif numoftickets > 10:
    priceperticket = 60
elif numoftickets > 5:
    priceperticket = 70
elif numoftickets < 5:
    priceperticket = 75

totalcost = numoftickets * priceperticket

print("Number Of Tickets: ", numoftickets)
print("Price Per Ticket: ", priceperticket)
print("Total Cost is: ", totalcost)