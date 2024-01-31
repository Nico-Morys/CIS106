name = input("Please Enter A Name: ")
costofapp = float(input("Please Enter The Cost Of The App: "))
warantee1 = .05
warantee2 = .10

if costofapp <= 1000:
    waranteecost = costofapp * warantee1 
    totalcost = waranteecost + costofapp
    print("Name:",name)
    print("Cost Of Application:",costofapp, "Warantee Cost:",waranteecost, "Total Cost:",totalcost)
elif costofapp > 1000:
    waranteecost = costofapp *warantee2
    totalcost = waranteecost + costofapp
    print("Name:",name)
    print("Cost Of Application:",costofapp, "Warantee Cost:",waranteecost, "Total Cost:",totalcost)