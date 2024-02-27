def sqmatrix(no):
    for i in range(no, 0, -1):
        for x in range(1, i + 1):
            print(x, end="")
        print("")


number = int(input("Whats the value of N:  "))
sqmatrix(number)
