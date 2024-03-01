def sqmatrix(no):
    for i in range(0, no + 1, 1):
        spaces = (" " * (no - i)) * 2
        stars = "*" * i
        print(stars + spaces + stars)
    for i in range(no - 1, 0, -1):
        spaces = (" " * (no - i)) * 2
        stars = "*" * i
        print(stars + spaces + stars)


number = int(input("Whats the value of N:  "))
sqmatrix(number)
