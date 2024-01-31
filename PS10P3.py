f = open("txtfile1.txt", "r")


lastn = []
scores = []

lastname = f.readline()

def display(lastn, scores):
    l = len(lastn)
    high_var = -1
    low_var = 999
    for i in range (0, l, 1):
        if float(scores[i]) > float(high_var):
            high_var = scores[i]
            high_index = i

        if float(scores[i]) < float(low_var):
            low_var = scores[i]
            low_index = i
            
    print("Highest Score: ", lastn[high_index], scores[high_index])
    print("Lowest Score: ", lastn[low_index], scores[low_index])




while lastname !="":
    lastn.append(str(lastname).rstrip("\n"))
    s = float(f.readline())
    scores.append(s)
    lastname = f.readline()
display(lastn, scores)


