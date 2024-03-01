def sqmatrix(no):
    for i in range(1, no + 1, 1):
        for x in range(1, i + 1):
            print(x, end="")
        for x in range(2 * (no - i), 0, -1):
            print(" ", end="")
        for x in range(i, 0, -1):
            print(x, end="")
        print("")


number = int(input("What's the value of N: "))
sqmatrix(number)
