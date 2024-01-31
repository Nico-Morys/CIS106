lastname = input("Please Enter The Last Name: ")
game1 = float(input("Please Enter Game 1's Score: "))
game2 = float(input("Please Enter Game 2's Score: "))
game3 = float(input("Please Enter Game 3's Score: "))
handicap = float(input("Please Enter The Handicap Percentage In Decimal: "))

def comp(game1, game2, game3, handicap):
    avg = (game1 + game2 + game3) / 3
    avgh = ((game1 + game2 + game3) * handicap) / 3

    return avg, avgh

avg, avgh = comp(game1, game2, game3, handicap)

print(lastname)
print("Average Score Before Handicap: ", avg)
print("Average Score After Handicap: ", avgh)

