f = open("datatext2.txt", "r")

sumtuition = 0
sumstudents = 0


lastname = str(f.readline().rstrip('\n'))

while lastname !="":
    district = str(f.readline().rstrip('\n'))
    credits = float(f.readline())

    
    if district == "I":
        costpercredit = 250
    elif district == "O":
        costpercredit = 500


    tuitionowed = credits * costpercredit
    print("Last Name: ", lastname)
    print("Credits Taken: ", credits)
    print("Tution Owed: ", tuitionowed)

    sumtuition = sumtuition + tuitionowed
    sumstudents = sumstudents + 1

    lastname = str(f.readline().rstrip('\n'))


print("Sum Of Tuition: ", sumtuition)
print("Number Of Students: ", sumstudents)

