principleamount = float(input("Please Enter A Principle Amount: "))
yeartomat = int(input("Please Enter The Years To Maturity: "))

if principleamount > 100000 and yeartomat == 5:
    interestrate = .06
elif principleamount > 50000 and yeartomat == 10:
    interestrate = .05
elif principleamount > 50000 and yeartomat == 5:
    interestrate = .04
else: interestrate = .02

interestamount = principleamount * interestrate 

print("Principle: ", principleamount)
print("Interest Rate: ", interestrate)
print("First Year Interest Amount: ", interestamount)
