f = open("txtfile2.txt", "r")

lastn = []
batavg = []

lastname = f.readline()

def search(lastn, sname):
    l = len(lastn)
    sindex = -1
    for y in range(0, l, 1):
        if lastn[y] == sname:
            sindex = y
    return sindex 

def display(lastn, batavg):
    l = len(lastn)
    high_var = -1
    low_var = 999
    for i in range (0, l, 1):
        if float(batavg[i]) > float(high_var):
            high_var = batavg[i]
            high_index = i

        if float(batavg[i]) < float(low_var):
            low_var = batavg[i]
            low_index = i
            
    print("Highest Score: ", lastn[high_index], batavg[high_index])
    print("Lowest Score: ", lastn[low_index], batavg[low_index])


while lastname !="":
    lastn.append(str(lastname).rstrip("\n"))
    s = float(f.readline())
    batavg.append(s)
    lastname = f.readline()
display(lastn, batavg)

response = input("Do You Want To Search For A Batting Avg? Enter Yes or No: ")

while response == "Yes":
    sname = input("Please Enter A Players Last Name: ")
    i = search(lastn, sname)
    if i == -1:
        print("Wrong Name")
    else:
        print(lastn[i], " avg of ", batavg[i])
    response = input("Do you want to do this again? Enter Yes or No ")
