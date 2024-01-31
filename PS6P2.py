def fib(n):
    a = 0 
    b = 1

    for count in range(1,n):
        c = a + b
        a = b
        b = c 
        print(c)

fib(20)