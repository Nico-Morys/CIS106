response = input("Would you like to start? Please Enter Yes or No: ")

while response == "Yes":
    length = float(input("Please Enter the Length: "))
    width = float(input("Please Enter the Width: "))
    height = float(input("Please Enter the Height: "))
    response = input("Would you like to do this again? Please Enter Yes or No: ")

def compsquare(length, width, height):
    squarefootage = (2 * length * width) + (2 * length * height) + (2 * width * height)

    return squarefootage

squarefootage = compsquare(length, width, height)

gallonsneeded = squarefootage / 50

print("You will need", gallonsneeded, "gallons of paint")