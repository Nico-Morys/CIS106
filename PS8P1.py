response = input("Would You like Start? Please Type Yes or No: ")


while response == "Yes":
    lastname = input("Please Enter Your Last Name: ")
    month = input("Please Enter The Month: ")
    sales = float(input("Please Enter The Amount of Sales: "))
    response = input("If you would like to do another month please type Yes or No: ")


def compforecast(month, sales):
    if month == "January":
        percent = 0.10
    elif month == "Febuary": 
        percent = .10
    elif month == "March":
        percent = .10
    elif month == "April":
        percent = .15
    elif month == "May":
        percent = .15
    elif month == "June":
        percent = .15
    elif month == "July": 
        percent = .20
    elif month == "August": 
        percent = .20
    elif month == "September":
        percent = .20
    elif month == "October":
        percent = 0.25
    elif month == "November":
        percent = .25
    elif month == "December":
        percent = .25
    
    nextmonthsales = sales * (1 + percent)

    return nextmonthsales

nextmonthsales = compforecast(month, sales)


print("Next Months Sales: ", nextmonthsales)