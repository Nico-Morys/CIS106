principle = float(input("Please Enter A Principle Amount: "))
interestrate = float(input("Please Enter A Interest: "))


for count in range(1, 6, ): 
    interest = principle * interestrate
    endingbal = principle + interest
    print(count, "   ", principle, "   ", endingbal)
    principle = endingbal
