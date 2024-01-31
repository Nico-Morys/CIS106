lastname = input("Please Enter A Last Name: ")
jobcode = input("Please Enter A Job Code L, A, or J: ")
hoursworked = float(input("Please Enter The Amount Of Hours Worked: "))

def comprop(jobcode, hoursworked):
    if jobcode == "L":
        payrate = 25
    elif jobcode == "A":
        payrate = 30
    elif jobcode == "J":
        payrate = 50
    else: print("Please Enter A Correct Job Code...")

    return payrate

payrate = comprop(jobcode, hoursworked)

def compgross(hoursworked, payrate):
    if hoursworked > 40:
        overtime = (hoursworked - 40) * (payrate * 1.5)
        finalpay = (40 * payrate) + overtime
    else: finalpay = hoursworked * payrate

    return finalpay

finalpay = compgross(hoursworked, payrate)

print(lastname)
print("Gross Pay is: ", finalpay)

