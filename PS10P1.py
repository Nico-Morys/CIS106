def displaynamesr(lastname):
    reverse = lastname[::-1]
    for i in range(len(lastname)):
        print(reverse[i])


def displaynames(lastname):
    for i in range(len(lastname)): 
        print(lastname[i])


lastname = ["Cook", "James", "Fox", "Kopec", "Knight", "Culler", "Decker", "McFly", "Gravy", "Chubb"]
displaynames(lastname)
displaynamesr(lastname)
 