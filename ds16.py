def sqmatrix(no):
    for i in range(1, no + 1, 1):
        for j in range(i, 65 + i):
            n = chr(j)
        print(n * i)


number = int(input("Whats the value of N:  "))
sqmatrix(number)


def sqmatrix1(no):
    for i in range(no):
        for j in range(i + 1):
            print(chr(65 + i), end="")
        print("")


number = int(input("What's the value of N: "))
sqmatrix1(number)
