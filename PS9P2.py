lastname = input("Please Enter a Last Name: ")
exam1 = float(input("Please Enter Exam 1's Score: "))
exam2 = float(input("Please Enter Exam 2's Score: "))
exam3 = float(input("Please Enter Exam 3's Score: "))


def compavg(exam1, exam2, exam3):
    avg = (exam1 + exam2 + exam3) / 3
    totalpoints = (exam1 + exam2 + exam3)

    return avg, totalpoints

avg, totalpoints = compavg(exam1, exam2, exam3)

print(lastname)
print("Average Exam Score is: ", avg)
print("Total Points: ", totalpoints)