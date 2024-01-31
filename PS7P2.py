lastname = input("Please Enter A Last Name: ")
numhits = float(input("Please Enter The Number Of Hits: "))
numbats = float(input("Please Enter The Number At Bats: "))



def compavg(numhits, numbats):
    batavg = numhits / numbats

    return batavg

batavg = compavg(numhits, numbats)

print(lastname)
print("Batting Average: ", batavg)