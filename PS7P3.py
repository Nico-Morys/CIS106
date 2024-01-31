destination = input("Please Enter The Destination: ")
milestrav = float(input("PLease Enter The Miles Traveled: "))
gallonsused = float(input("Please Enter The Amount Of Gallons Used: "))
cpg = float(2.50)


def compmpg(milestrav, gallonsused):
    mpg = milestrav / gallonsused
    
    return mpg

mpg = compmpg(milestrav, gallonsused)

def compcost(gallonsused, cpg):
    costofgas = float(gallonsused) * float(cpg)

    return costofgas

costofgas = compcost(gallonsused, cpg)

print(destination)
print("Miles Traveled: ", milestrav)
print("MPG: ", mpg)
print("Cost Of Gas: ", costofgas)