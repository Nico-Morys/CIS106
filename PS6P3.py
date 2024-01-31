f = open("datatext.txt", "r")

bonusrate1 = .20
bonusrate2 = .15
bonusrate3 = .10
sum1 = 0

lastname = f.readline()

while lastname != "":
    salary = float(f.readline())
    if salary >= 100000:
        bonus = float(salary) * bonusrate1
    elif salary >= 50000:
        bonus = float(salary) * bonusrate2
    elif salary < 50000:
        bonus = float(salary) * bonusrate3
    print("Employee Last Name", lastname)
    print("Employee Salary: ", salary)
    print("Employee Bonus: $", bonus)
    
    
    lastname = f.readline()
    sum1 = sum1 + bonus


print("Total Paid Out: ",sum1)
