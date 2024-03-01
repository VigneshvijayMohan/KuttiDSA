def sqmatrix(no):
    for i in range(1, no + 1):
        print(" " * (no - i), end="")
        for x in range(i):
            print(chr(65 + x), end="")

        for x in range(i - 2, -1, -1):
            print(chr(65 + x), end="")

        print(" ")


number = int(input("What's the value of N: "))
sqmatrix(number)
