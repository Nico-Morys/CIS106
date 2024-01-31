response = input("Would You like Start? Please Type Yes or No: ")

while response == "Yes":



    lastname = input("Please Enter A Last Name: ")
    credithours = float(input("Please Enter The Credit Hours: "))
    districtcode = input("Please Enter A District Code I or O: ")
    response = input("Would You like Start? Please Type Yes or No: ")

def compcost(credithours, districtcode):
    if districtcode == "I":
        cph = 250
        tuitionowed = credithours * cph
    elif districtcode == "O":
        cph = 550
        tuitionowed = credithours * cph


    return tuitionowed

tuitionowed = compcost(credithours, districtcode)

print(lastname)
print("Tuition Owed is: ", tuitionowed)