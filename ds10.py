def sqmatrix(no):
    for i in range(1, no + 1, 1):
        spaces = " " * ((no * 2 - 1 - i) // 2)
        stars = "*" * i
        print(stars + spaces)

    for i in range(no - 1, 0, -1):
        spaces = " " * ((no * 2 - 1 - i) // 2)
        stars = "*" * i
        print(stars + spaces)


number = int(input("Whats the value of N:  "))
sqmatrix(number)
