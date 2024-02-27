def sqmatrix(no):
    for i in range(no):
        for j in range(i + 1):
            print(chr(65 + i), end="")
        print("")

number = int(input("What's the value of N: "))
sqmatrix(number)
