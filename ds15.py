def sqmatrix(no):
    for i in range(no, 0, -1):
        for x in range(65, 65 + i):
            print(chr(x), end="")
        print("")

number = int(input("What's the value of N: "))
sqmatrix(number)
