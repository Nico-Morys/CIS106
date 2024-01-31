counter = 0

response = input("If you want to calculate the averaging score please enter Yes or No: ")

while response == "Yes":
    counter = counter + 1
    lastname = input("Enter a Last Name please: ")
    examscore1 = float(input("Enter an exam score: "))
    examscore2 = float(input("Enter a second exam score: "))
    averagescore = (examscore1 + examscore2) / 2
    print(lastname, "average score is", averagescore)
    response = input("Do you want to calculate an average again? If so please enter Yes or No: ")

print("Number of students: ", counter)