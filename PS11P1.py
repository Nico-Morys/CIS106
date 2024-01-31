def dl1 (mylist):
    n = int(input("Please Enter a Number of Items For Your List: "))
    for n in range(0, n, 1):
        s = int(input("Enter a Number: "))
        mylist.append(s)
    return mylist
def displaylist(mylist):
    for item in mylist:
        print(item)




mylist = []
myulist = dl1(mylist)
displaylist(mylist)
print(mylist)

mylist.insert(0,99)
print(mylist)

mylist[0] = 100
print(mylist)

mylist2 = [500, 600, 700, 800, 900]
mylist2.extend(mylist)
print(mylist2)

mylist2.remove(800)
print(mylist2)

del mylist2[2]
print(mylist2)

mylist3 = ["A", "B", "C", "A", "A", "C"]
print("Number of A grades", mylist3.count("A"))                
print("Position of the first B Grade", mylist3.index("B"))

if "F" in mylist3:
    print("There is a grade F")          
else: print("F is not in the list")

mylist2.clear()                            
print(mylist2)

del mylist2                 #error will pop up because list is being deleted then trying to be printed
print(mylist2)             


mylist4 = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
mylist4.sort()
print(mylist4)

players2 = mylist4.copy()
print(players2)

players2.reverse()
print(mylist4)
print(players2)







