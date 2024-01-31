response = input("Would you like to determine the value percent? Please Enter Yes or No: ")
sum = 0
marketvalues = 0

while response == "Yes":
    county = input("What County Are You In? ")
    marketvalue = float(input("Please Enter The Market Value of the Home: "))

    def compvalue(county, marketvalue):
        if county == "Cook":
            percent = .90
        elif county == "DuPage":
            percent = .80
        elif county == "McHenry":
            percent = .75
        elif county == "Kane":
            percent = .60
        else: percent = .70
        
        assessedvalue = marketvalue * percent
    
        return assessedvalue
    
    assessedvalue = compvalue(county, marketvalue)
    sum = sum + assessedvalue
    marketvalues = marketvalues + marketvalue
    response = input("Would you like to determine the values of another home? Please Enter Yes or No: ")

print("All Market Values: ", marketvalues)
print("Assessed Values: ", assessedvalue)


