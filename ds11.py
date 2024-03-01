def sqmatrix(no):
    for i in range(1, no + 1):
        for j in range(i):
            if (i + j) % 2 == 0:
                print("0", end="")
            else:
                print("1", end="")
        print("")


number = int(input("Whats the value of N:  "))
sqmatrix(number)
