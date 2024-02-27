def sqmatrix(no):
    for i in range(1, no + 1, 1):
        for x in range(1, i + 1):
            print(x, end="")
        print("")


number = int(input("Whats the value of N:  "))
sqmatrix(number)
