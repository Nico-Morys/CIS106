f = open("datatext1.txt", "r")

sumextended = 0
count = 0

itemname = str(f.readline().rstrip('\n'))

while itemname !="":
    quantity = float(f.readline())
    price = float(f.readline())
    
    extendedprice = quantity * price
    sumextended = sumextended + extendedprice
    count = count + 1
    
    
    
    print("Item: ", itemname)
    print("Quantity: ", quantity)
    print("Price of item: ", price)
    print("Extended Price is: ", extendedprice)

    itemname = str(f.readline().rstrip('\n'))

avg = sumextended / count

print("Total Extended Prices: ", sumextended)
print("Total Number of Orders: ", count)
print("Average Order is: ", avg)

