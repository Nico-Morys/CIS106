lastname = input("Please Enter The Last Name: ")
creditstaken = float(input("Please Enter How Many Credits Were Taken: "))
credithour = int(250)
labfee = int(100)
totaltuition = (creditstaken * credithour + labfee)

print(lastname , "Total Tuition Cost Is: $" ,totaltuition)
