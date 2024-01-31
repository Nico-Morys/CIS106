def displaynames(lastname, scores):
    for i in range(len(lastname)): 
        print(lastname[i],"  ",scores[i])


lastname = ["Cook", "James", "Fox", "Kopec", "Knight", "Culler", "Decker", "McFly", "Gravy", "Chubb"]
scores = [74, 55, 91, 92, 84, 100, 65, 98, 76, 90]
displaynames(lastname, scores)