def sqmatrix(no):
    for i in range(no+2):
        for x in range(64+ i,64,  -1):
            # print(x)
            print(chr(x), end="")
        print("")



def something(num):
    for i in range(num, 0, -1):
        for x in range(i):
            print(chr(64 + i), end="")
        i -= 1
        print("")
    
    
number = int(input("What's the value of N: "))
something(number)
