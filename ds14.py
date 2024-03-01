def sqmatrix(no):
    for i in range(1, no + 1):
        for x in range(65, 65 + i):
            print(chr(x), end="")
        print("")


number = int(input("What's the value of N: "))
sqmatrix(number)
