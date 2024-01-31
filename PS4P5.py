lastname = input("Please Enter The Employee Last Name: ")
salary = float(input("Please Enter The Employee's Salary: "))
joblevel = int(input("Please Enter The Employee's Job Level: "))

if joblevel >= 10:
    bonusrate = .25
elif joblevel > 5:
    bonusrate = .20
else: bonusrate = .10

bonus = salary * bonusrate

print("Employee's Last Name: ", lastname)
print("Employee's Bonus: ", bonus)